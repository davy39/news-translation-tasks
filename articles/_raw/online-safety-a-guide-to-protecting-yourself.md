---
title: Online Safety – A Guide to Protecting Yourself
subtitle: ''
author: Rohit Jacob Mathew
co_authors: []
series: null
date: '2024-05-20T15:13:00.000Z'
originalURL: https://freecodecamp.org/news/online-safety-a-guide-to-protecting-yourself
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/rohit-2400-x-1260.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: Security
  slug: security
seo_title: null
seo_desc: "Navigating digital accounts safely is a concern for many in the modern\
  \ age. \nDigital accounts have become an integral part of our daily lives. From\
  \ email and online banking to accounts on ride-sharing platforms like Uber and e-commerce\
  \ platforms like..."
---

Navigating digital accounts safely is a concern for many in the modern age. 

Digital accounts have become an integral part of our daily lives. From email and online banking to accounts on ride-sharing platforms like Uber and e-commerce platforms like Amazon, protecting our digital lives online is becoming imperative.

When computing began, we used computers for complex calculations on individual machines. 

Gradually, we started connecting these machines through the internet, leading to the dot-com boom. This boom resulted in the creation of many websites like chat rooms and forums. 

To access these, you needed to identify yourself, which led to the use of the common username and password system we use today to create accounts. 

This username and password became a way to uniquely identify a person and their account on these sites, forming a type of digital identity.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-47.png)
_Common Cyber Attack Vectors ([Source](https://www.balbix.com/insights/attack-vectors-and-breach-methods/))_

Nowadays, some of the most common incidents we see are phishing scams, identity theft, [socially engineered attacks](https://www.cisco.com/c/en/us/products/security/what-is-social-engineering.html), ransomware, and compromised or weak credentials. Most, if not all, of these are directly or indirectly related to our digital identity and how we access it. Therefore, we need to ensure we secure ourselves online.

## How To Secure Yourself Online? 🙋

I will discuss one aspect of securing yourself online, which relates to digital accounts and how we access them. The most recommended strategy for that is:

1. Use a Passwordless login method like Face ID, Fingerprint Login, or Passkeys.
2. Use a password manager, like BitWarden or 1Password, for sites that still require a username and password.
3. Implement multi-factor authentication (MFA) to verify your identity. This can include a Time-Based OTP (TOTP) or a deep link verification through email.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-48.png)
_Table From Bad To Good On Protecting Your Account ([Source](https://www.microsoft.com/en-us/security/business/solutions/passwordless-authentication))_

Let me also share the strategy I use:

* I currently use 1Password as my password manager.
* I have TOTP or Passwordless MFA implemented on most sites.
* I have removed most social logins and Single Sign-On.
* I regularly conduct a security audit to see who has access to my data.
* In the event of a data leak or hack, I immediately change my passwords.
* Passwordless account creation using passkeys is a recent improvement, and I will likely start adopting them soon.

## But ... 🤔 I'm Still Confused. Why Should We Do All This?

Good question. Let's explore why we find password-based logins inefficient, inconvenient, and frustrating.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-49.png)
_Login &amp; Signup Page_

Let's start with a login screen. You see above the traditional username/password login or signup page and a few [social logins](https://blog.rohitjmathew.space/why-is-a-social-login-more-secure). These are currently the most common methods of accessing an account. 

Let's examine how these methods contribute to feelings of inefficiency, inconvenience, and frustration.

### Inefficient

* **We Create Terrible Passwords -** Below are some of the most common passwords in the world. There are open-source lists of these passwords that hackers use. Simple passwords like these or those related to you are not secure at all. They can easily be guessed from the list or with a little social engineering.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-50.png)
_Common Passwords In The World ([Source](https://www.quora.com/Is-using-password-as-a-password-really-common))_

* **We Reuse the Same Passwords -** To make things easier, we often use the same passwords for multiple accounts. This is very insecure because if one account is compromised, a hacker can easily access other accounts.
* **Compromised Social Logins -** While social logins are easier to use, they also present a single point of failure. If one social login is compromised, it can lead to other accounts being compromised as well.
* **SMS & Voice-Based Multi-Factor Authentication (MFA) Can Be Hacked -** While MFA has improved security, hackers have adapted and found ways to intercept SMS or voice-based MFA. Therefore, these methods are no longer the most secure.

**_Note:_** _If you visit the site_ [_haveibeenpwned_](https://haveibeenpwned.com), _you can see which of your data has been compromised._

### Inconvenient

* **Resetting Passwords is Not Easy -** When we forget our passwords, we often have to go through multiple steps to regain access to our accounts.
* **Password Requirements Are Sometimes Hard To Remember -** Creating a new password that meets all the security requirements, such as including uppercase letters, numbers, and special characters, can be difficult to remember.
* **Social Logins Might Not Work Sometimes -** With recent downtimes of social media sites, your logins might also face interruptions.
* **Multi-Factor Authentication (MFA) Can Add Friction -** MFA often requires an extra step and is linked to a device, which can complicate the process. Additionally, backing up and recovering MFA methods is not straightforward.

### Frustrating

* **Remembering Different Passwords -** Memorable passwords are easy for hackers to guess or crack. It's frustrating to have different passwords for various accounts and to remember each one.
* **Social Login Providers & Data Privacy -** Some social login providers or websites may share or sell their user data to third-party entities. This means that when you use social logins, your personal information, browsing habits, and other data, might be accessed by companies you didn't intend to share it with.
* **Multi-Factor Authentication (MFA) Not Working -** SMS or voice call containing the authentication code not being received, delays in receiving push notifications, or Time-based One-Time Passwords (TOTP) can expire are a few examples. These issues can cause significant frustration and hinder the login process.
* **Multi-Factor Authentication (MFA) Abuse -** There has been an increase in hackers abusing MFA to access accounts. They exploit MFA solutions that send sign-in approval notifications after account access attempts, knowing that people often get frustrated by a flood of messages. Hackers have breached [Uber](https://www.wired.com/story/uber-hack-mfa-phishing/), [Microsoft, and Cisco](https://tech.co/news/mfa-fatigue-hackers) using this method.

## Right, So Why Is The Recommended Strategy Better? 😅

Let's break down the recommended strategy:

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-48.png)
_Table From Bad To Good On Protecting Your Account ([Source](https://www.microsoft.com/en-us/security/business/solutions/passwordless-authentication))_

### Use a Passwordless Login Method

Passwordless methods are more secure than password-based logins. If you want to know why, you can read my article on [How Does Face ID or Touch ID Work](https://blog.rohitjmathew.space/intro-to-webauthn). 

In simple terms, passwordless methods, like Passkey, use biometric authentication along with device identifiers to enable multifactor authentication (something you are and something you have) instead of a password (something you know).

This approach is not only easier and more secure but also resistant to many of the issues we discussed earlier. Although still new, there has been a significant industry push to adopt this, especially with the rise of biometric authenticators in our devices.

_**Note:** You can find a list of websites and apps that support passwordless login or MFA, along with instructions on how to set it up, at [passkeys.directory](https://passkeys.directory/)._

### Use a Password Manager for Sites That Still Require a Username and Password

While not every site has adopted passwordless logins, a better way to secure your accounts that still use passwords is by using a password manager like [Bitwarden](https://bitwarden.com/) or [1Password](https://1password.com/). 

They help you create strong, unique passwords and remember them easily. Most password managers come with autofill features that make it easy to use across devices.

While they can be a single point of failure and might be a bit of a hassle to set up initially, the benefits far outweigh the drawbacks. 

Remembering just one master password to manage your accounts securely is much better than dealing with the issues mentioned earlier.

**_Note:_** _1Password (the password manager I use) has provided more_ [_details_](https://blog.1password.com/what-if-1password-gets-hacked/) _on what happens if they are hacked. While there have been recent_ [_hacking incidents_](https://www.forbes.com/sites/daveywinder/2023/10/24/no-1password-has-not-just-been-hacked-your-passwords-are-safe/)_, I am not aware of any compromised data._

### Implement Multi-factor Authentication to Verify Your Identity

Multi-factor Authentication (MFA) is a security measure that requires users to provide more than one form of identification to access their accounts. 

This typically involves a combination of something you know, like a traditional password, and something you have, such as a one-time password (OTP) sent via SMS or email. 

By adding this extra layer of security, MFA significantly reduces the risk of unauthorized access, even if your password is compromised.

![Image](https://www.freecodecamp.org/news/content/images/2024/05/image-51.png)
_What Is Multi-factor Authentication ([Source](https://www.hsph.harvard.edu/information-technology/2022/10/03/october-is-cybersecurity-month-week-1/))_

Implementing MFA is a crucial step in protecting your online accounts and personal information. It may take a bit of extra time during the login process, but the added security is well worth the effort.

**_Note:_** _Most websites and services we use provide 2FA. You can check based on your use case at_ [_2fa.directory_](https://2fa.directory/)_._

## Conclusion

This article explores common security threats and offers strategies to protect yourself online. 

Some recommendations include using passwordless login methods like Face ID or Passkeys, using password managers like 1Password, and implementing multi-factor authentication (MFA). 

These measures can greatly improve your online security and reduce the risk of unauthorized access to your accounts.

Hopefully, this article helps you understand why online security is important and enables you to stay safe on the internet.

Thanks for reading! I really hope that you find this article useful. If you think this post was useful, please share the post to help promote this piece to others.

If you want to read more of my articles, visit my [**blog**](https://blog.rohitjmathew.space/)**.**

Thanks again for reading! :)

P.S Do feel free to connect with me on [**LinkedIn**](https://www.linkedin.com/in/rohitjmathew) or [**Twitter**](https://twitter.com/iamrohitjmathew).

