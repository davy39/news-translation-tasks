---
title: How to Prevent Account Loss When using Two-Factor Authentication
subtitle: ''
author: Obum
co_authors: []
series: null
date: '2023-03-22T16:28:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-prevent-account-loss-when-using-two-factor-authentication
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/pexels-karolina-grabowska-4467737.jpg
tags:
- name: Security
  slug: security
- name: Two-factor authentication
  slug: two-factor-authentication
seo_title: null
seo_desc: "If someone gains unauthorized access to your passwords, two-factor authentication\
  \ (2FA) can prevent them from accessing your account. \nBut if you ever lose access\
  \ to all your 2FA methods, you have lost your account. How do you prevent such loss?\n\
  In t..."
---

If someone gains unauthorized access to your passwords, two-factor authentication (2FA) can prevent them from accessing your account. 

But if you ever lose access to all your 2FA methods, you have lost your account. How do you prevent such loss?

In this article, we will look at two-factor authentication (2FA), its methods, and how to prevent account loss because of using it.

## Table of Contents

* [What is Two-Factor Authentication (2FA)](#heading-what-is-two-factor-authentication-2fa)?
* [Methods of Two-Factor Authentication](#heading-methods-of-two-factor-authentication)
* [The problem with Two-Factor Authentication](#heading-the-problem-with-two-factor-authentication)
* [How to Protect Yourself from Losing Access to Your Accounts](#heading-how-to-protect-yourself-from-losing-access-to-your-accounts)  
1. [Backup and write down the recovery code(s)](#heading-1-backup-and-write-down-the-recovery-codes)  
2. [Backup and write down the authenticator app seed](#heading-2-backup-and-write-down-the-authenticator-app-seed)  
3. [Set up more than one 2FA method](#heading-3-set-up-more-than-one-2fa-method)  
4. [Always update 2FA methods](#heading-4-always-update-2fa-methods)  
5. [Set up recovery email and phone](#heading-5-set-up-recovery-email-and-phone) 
* [Summary](#heading-summary)

## What is Two-Factor Authentication (2FA)?

Two-Factor Authentication is an extra security setting for your account that many platforms have enabled. 

It is an extra security setting because you already have some "first" way of authenticating yourself. This "first" way could be password sign-in or federated identity sign-in. Federated identity means signing in with another provider, like Apple, Facebook, Google, and so on.

Two-Factor authentication helps reduce unauthorized access to your data or account. It is a second sign-in step to verify that you are the owner of the account. So, in addition to your first sign-in method, you will have to complete this second step (hence two-factor) to access your account.

Two-Factor authentication is not about using and securing your passwords. That one is basic account security. We are talking about an advanced security step where, after entering your password, you still need to enter some code or complete some action before you gain access to your account. 

In this article, platform means any place where you can sign in and sign out. freeCodeCamp, LinkedIn, and Twitter are examples of platforms. In this article, a platform is a place where you have an account.

Some platforms don't offer 2FA. You might have relatively little data with them. So 2FA would be overkill there. On the other hand, the major and mainstream platforms where you can have an account offer 2FA. These are platforms where a user's account is worth hacking. 

In most platforms, 2FA is optional. In a few, however, you are required to set up 2FA from the very first time you access the account and you can't turn it off. In other words, 2FA is a must-do on a few platforms.

You should set up 2FA where it is available. To set up 2FA, go to the security settings of your account on a supporting platform. Set up 2FA using at least of one the specified methods and you are good to go. On subsequent sign-ins, you will need to complete 2FA to enter the account.

## Methods of Two-Factor Authentication

Methods of 2FA refer to the various ways to set up 2FA. They are as follows:

1. Security Key 2FA
2. Phone number 2FA
3. Authenticator app 2FA
4. Sign-In prompt
5. Recovery code(s)

Security keys are USB or Bluetooth keys that you can connect to your device. They are physical 2FA devices and seem to be the most secure. This is because it is highly unlikely that a hacker would come and steal the key from your house. 

To set up 2FA using keys, plug in the key or connect via Bluetooth and complete the steps. You can then use the key in consequent sign-ins. You have to buy these keys from the market or online to use them. 

Phone number 2FA involves receiving a One-Time Password (OTP) code either via call or SMS. Provide a phone number and the platform sends an OTP to it. Sometimes, you could receive an automated call with the code. Either way, enter the code in the platform and you have successfully set up the phone number 2FA. 

On subsequent sign-ins to access your account, after entering your password, you will receive an OTP code to that phone. Enter the code to gain access to your account.

Authenticator apps generate a 6-digit code every minute. [There are many authenticator apps](https://www.google.com/search?q=authenticator+apps), like Google Authenticator, Microsoft Authenticator, and others. 

To set up an authenticator app, you either scan a QR code or enter a seed phrase. The platform where your account resides will provide you with either of these. Scan or enter the phrase and you will keep getting a unique 6-digit code every minute. 

In the next sign-ins, after entering your password, paste the latest 6-digit code from the authenticator app and you are in.

Sign-in prompts are not as common as other 2FA methods. Not all platforms have this feature. It involves authorizing your sign-in from an app or website of that platform where you are already signed in. 

GitHub and Google have these features. With the GitHub app, you can complete 2FA by entering a number on the screen from the app/website you signed in to. Google does it together with your Android device and your Google account.

Aside from the above 2FA methods, we also have recovery codes. Recovery codes are a one-time-use code that you can use to complete 2FA. You can access them under the 2FA settings of your account.

In fact, once you set at least one 2FA method on your account, the platform autogenerates these recovery codes for you. These codes are like a backup option for 2FA. You are meant to use them when you don't have access to the other 2FA methods.

## The Problem with Two-Factor Authentication

The problem with 2FA is that if you lose access to all the methods you've set up, **you've permanently lost access** to that account. Let me explain.

2FA ensures that it is the correct user that is accessing an account. That's why we have those above secondary methods aside from your password. 2FA can only be enabled or disabled while signed in. 

But aside from the recovery codes, there is no other recovery mechanism. If you lose the security keys, phone number, devices with the authenticator apps and previous sign-ins, and the recovery codes, your account is gone. Not even the account support for that platform can help you. 

This is not the common "Forgot Password" feature, where the platform sends a unique link or code to your email or phone to reset your password. This is 2FA. Once you lose all 2FA methods you had set, your account is gone. Support can't give you the recovery codes because they don't know them. Those codes are encrypted with your account's access (only you can access them when you are signed in).

Does this mean that you shouldn't set up 2FA? 

No. It means that in addition to setting up 2FA, you have to guard your 2FA methods. Remember that it is security that led us to 2FA. Well, 2FA itself also needs security. So you have to secure it.

From here, we will be looking at the various things you can do to prevent account loss due to Two-Factor Authentication.

## How to Protect Yourself from Losing Access to Your Accounts

### 1. Backup and write down the recovery code(s)

All platforms that grant 2FA also give a recovery code(s). Always back them up. Copy and save the recovery codes securely somewhere of your choice. Hide them discretely online. Encrypt them in some vaulted storage. 

Most importantly, **write** them down. Like use your hand and write with a pen in some diary or book you won't lose. You can equally print and store them with your documents and certificates. Just protect each recovery code per platform in the most secure way you're able.

Also, don't store the recovery code of an account in that same account. No one keeps spare keys inside the house. You give out your spare keys to trusted persons or keep them in other places where you can go retrieve them when need be. This is because if your main key goes missing while you are out, you can go and retrieve the spares. You can't retrieve the spare keys when they are inside the house and you are locked out.

In the same vein, it makes no sense to keep the recovery codes of your Google Account's 2FA inside your account's Google Drive or in a private Google Doc owned by the same account. When you will need it, you can't get it.

Recovery codes are **one-time-use** codes. You can't reuse the same recovery code for another 2FA session. You shouldn't really be using your recovery codes. If you start using them, it is a sign that you need to either update your 2FA methods, turn off 2FA temporarily, or regenerate a new set of recovery codes (to replace the used ones).

You can always copy out your recovery codes. Also, you can always generate a new set of recovery codes in each platform. Every platform permits that. Remember that you have to be signed in to do all these things. 

Also, anytime you disable or turn off two-factor authentication in your account settings, the previous recovery codes become invalid. If you enable 2FA again, you will need to re-backup and re-write the new recovery codes.  

Make sure you store recovery code(s) for each platform in multiple and different places. 

### 2. Backup and write down the authenticator app seed

When setting up the authenticator app 2FA, don't use the QR code option. Go for the seed option. The seed for authenticator apps comes as a series of about 20 to 40 alphanumeric characters. When the platform shows you this seed, first **write** it down. 

Write down the authenticator app seed in your diary or in some book you've set aside for backup. If possible, copy it out and print it. Equally backup the seed for each platform in some other online media where you can retrieve it from. You want to minimize your chances of losing these seeds. 

Each minute, authenticator apps generate 6-digit codes **based on the seed** and not based on the app itself or the platform. If you paste that same seed into another authenticator app, the two apps will be generating the exact same 6 digits, every minute. In fact, if you re-use that exact same phrase to recreate another 2FA entry in the same authenticator app, the two entries will be generating the same 6-digit code per minute.

This is why the authenticator app seed is as important as the 2FA recovery codes. If you lose access to the device that your 2FA authenticator app is on, you can put your seeds in another authenticator and get back the 6-digit codes for 2FA. Protect these seeds too. Because if someone has both your passwords and seeds, then they have access to your accounts.  

Backing up and writing down authenticator app seeds is necessary and it is under-preached. Many people don't realize that device loss means account loss if the authenticator app was their only 2FA method and if they didn't save the seed and recovery codes somewhere. 

A device crash can happen. The Operating System might crash and you may lose apps and data. The authenticator app could be mistakenly uninstalled. Backing up and writing down the seeds prevent these circumstances from affecting your 2FA setups. 

You can reinstall the authenticator app and reconfigure the entries of each account from your saved seed, without needing to go to the account settings of each platform. Also, you will be capable of continuing to use your two-factor authentication methods, without needing to re-backup or re-write down a new set of recovery codes.

If you've already set up the authenticator app 2FA, and you didn't save the original seed your account's platform gave you, please, please, please go and reconfigure the authenticator app 2FA in your security settings. You might have to just disable only the authenticator app and turn it back on. While re-enabling, make sure you back up and write down the seed. You don't want to live the experience of being locked out of your account.

### 3. Set up more than one 2FA method

Setting up more than one method for two-factor authentication reduces your chances of account loss. The idea is to ensure that you always have access to at least one (if not all) 2FA methods. You can set up all the available 2FA methods per platform account. 

For USB/Bluetooth security key, you can use the same key for all your accounts across various platforms. For your phone number, you can use the same phone number across each account on each platform. (But some platforms don't permit you to have multiple accounts with the same phone number. Have this in mind if you fall into that category).

The authenticator app seed for each account per platform is different. But you can use the same authenticator app for all accounts in which you've set up 2FA. Just remember to back up and write down the seeds as mentioned in the previous section.

So for each platform, you want to ensure that you have set more than one 2FA method. You can receive an SMS with some phone number. You have a working authenticator app. You've backed up and written down the authenticator app seed and 2FA recovery codes. And where you can, you've equally set up the USB/Bluetooth security key.

### 4. Always update 2FA methods

Things can happen that warrant updating your 2FA methods. Updating 2FA methods include removing or adding some methods. You can equally change the settings of the same method. 

For example, let's say you never had a security key in your account. But you had set up 2FA with a phone number and authenticator app. Then you just bought a new security key. You can go and add the security key in your 2FA settings as a new method. On the other hand, if you lose your USB/Bluetooth security key, you can disable the security key option. Then when you buy a new one, you can put it back in your settings. 

If you lost your all backups and written-down versions of your authenticator app seeds and 2FA recovery codes, you can regenerate new ones and re-backup and re-write down. You really shouldn't lose everything. Such loss is not good. Well, anything is possible. Prevention is the only remedy as there is no cure in the world for complete 2FA loss. 

Also, it is okay to turn off 2FA if you need to. 2FA is recommended and necessary. But if you see the need to, turn it off for the moment. Then set it up back sometime later on. 

### 5. Set up recovery email and phone 

Backup email and phone are not really a 2FA thing. The reason is they are always there whether you configure two-factor or not. Most major platforms permit you to set a recovery email and or a recovery phone number for your account. These recovery assets come in handy when you forget your password and not when you lose 2FA.

Well, we are talking about security, so it is worth mentioning that you should have recovery email and phone properly set up where possible. 

In some platforms, your account or your recovery phone number can be different from your 2FA phone number. Your 2FA phone number must always be one where you can receive an OTP (via call or SMS) and use it to complete the 2FA step.

## Summary

You want to lock out malicious access to your account. But you don't want to lock out yourself.  

In this guide, we've looked at how to best use the two-factor authentication feature across various accounts. At the same time, we've also seen how you can ensure that you don't lose access to your account because you tried securing it in the first place.

Back up and write down recovery codes and authenticator app seeds. Set up multiple 2FA methods. Always review and update your 2FA settings. Do these and be rest assured of the best online security.

Cheers!

