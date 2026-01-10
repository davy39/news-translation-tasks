---
title: What is WebAuthn? How to Authenticate Users Without a Password
subtitle: ''
author: Rohit Jacob Mathew
co_authors: []
series: null
date: '2022-04-20T23:45:39.000Z'
originalURL: https://freecodecamp.org/news/intro-to-webauthn
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/webauthn.jpeg
tags:
- name: authentication
  slug: authentication
- name: passwords
  slug: passwords
seo_title: null
seo_desc: 'Most of us are used to logging into different accounts using a password.
  For years this has been the norm. But passwords face a number of security issues:


  They are extremely annoying when we don’t remember them and even harder to reset

  They can be q...'
---

Most of us are used to logging into different accounts using a password. For years this has been the norm. But passwords face a number of security issues:

* They are extremely annoying when we don’t remember them and even harder to reset
* They can be quite insecure with the most common password being `password` or `123456`
* Phishing attacks are commonplace in today’s internet era, and using this technique hackers can steal your passwords

Would it not be simpler to move towards a more passwordless login? A place where we don’t have to remember or have to enter passwords to gain access to our accounts? One such passwordless solution is WebAuthn.

## What is WebAuthn? 😅

The Web Authentication API (also known as WebAuthn) is an API that enables strong authentication with public-key cryptography. It lets you implement passwordless authentication and/or secure second-factor authentication without SMS texts.

Let’s break that down to quickly understand the parts:

* **Public Key Cryptography** — So we use a key-based authentication (public and private key) to login and not a password. If you are not sure how it works I suggest watching this [video](https://youtu.be/6-JjHa-qLPk?t=277).
* **Passwordless Authentication** — In this type of authentication we will not be using a password to login but will use some form of user interaction to verify and login. This uses a hardware authenticator like a fingerprint sensor on your device or a YubiKey.
* **Secure Second-Factor Authentication Without SMS Texts** — Two-Factor Authentication today is predominantly driven by SMS-based OTP, but these are also susceptible to SIM swap. SIM swap is essentially taking control of someone’s phone number, and tricking a carrier into transferring it to a new phone. A two-factor authentication scenario-driven through a hardware authenticator using WebAuthn would be a safer solution to the above problem.

WebAuthn is a specification written by the [W3C](https://www.w3.org/) and [FIDO](https://fidoalliance.org/), with the participation of Google, Mozilla, Microsoft, Yubico, and others. 

Web Authentication works hand in hand with other industry standards such as [Credential Management Level 1](https://www.w3.org/TR/credential-management-1/) and [FIDO 2.0 Client to Authenticator Protocol 2](https://fidoalliance.org/specs/fido-v2.0-rd-20170927/fido-client-to-authenticator-protocol-v2.0-rd-20170927.html).

## How Does WebAuthn Work? 🤔

So like every other login situation:

* A user would be prompted for a username to identify them.
* The browser would then prompt the user to use their hardware authenticator and verify themselves.
* On successful authentication, they would be logged into the system.

Now what we don’t often see is what goes on in the background to facilitate this process. Let me explain a little more.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/webauthn_flow_diagram.png)
_Generic WebAuthn Flow_

### Registration Flow

In this process, a new set of key credentials are created against the username entered by the user. This key credential is the crux of the process which enables us to make sure this authentication is in a passwordless manner.

There is a simple 8 step process that takes place:

1. A user clicks on the register button on a site on their browser (user agent).
2. The authenticating server (relying party) issues a challenge (a random set of data sent as an array) to the user’s browser to be able to enable WebAuthn login.
3. The browser sends this challenge to the authenticator device.
4. The authenticator device then prompts the user to authenticate themselves. This would be different based on the device, for example   Touch ID on a Macbook or touching a YubiKey.
5. Once the user authorizes the authenticator device, the authenticator will then create a new key pair (a public and private key) and will then use the private key to sign the challenge.
6. The authenticator device will then return the signed challenge, the public key as well as details pertaining to the process, back to the authenticating server.
7. The authenticating server will then confirm the authenticity of the private key by using the public key to ensure the challenge was signed by the private key.
8. It will then store the received details against the username for future use and respond that the user is registered.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Registration.png)
_Registration Flow_

### The WebAuthn Authentication Flow

Authentication is a similar process where the above-generated credentials are used to verify the user’s identity by going through a signed challenge process again.

There is a simple 8 step process that takes place:

1. A user clicks on the login button on a site on their browser (user agent) and enters their username.
2. The authenticating server (relying party) issues a challenge (a random set of data sent as an array) to the user’s browser along with the saved private key ID registered with the username.
3. The browser sends this challenge & private key ID to the authenticator device.
4. The authenticator device then prompts the user to authenticate themselves. This would be different based on the device (again,  Touch ID on a Macbook or touching a YubiKey).
5. Once the user authorizes the authenticator device, the authenticator will then retrieve the generated key pair saved on it with the provided private key ID. It will then use the private key to sign the challenge.
6. The authenticator device will then return the signed challenge as well as details pertaining to the process back to the authenticating server.
7. The authenticating server will then confirm the authenticity of the private key by using its saved public key to ensure the challenge was signed by the private key.
8. It will then log the user in.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Login.png)
_Authentication Flow_

## Benefits of WebAuthn

That sounds awesome, right? 😮 Absolutely. Let’s quickly see some of the benefits:

* **Private/Public Key Based Authentication** — It’s a more secure way to authenticate users compared to the current norm of password-based authentication as it uses asymmetric cryptography by default.
* **Phishing Resistant** — WebAuthn is resistant to phishing attacks due to the domain name being stored on the authenticator. This makes it harder for hackers to be able to spoof websites and gain access to credentials.
* **Store Public Data in Your DB** — Only public data is stored in the DB. No sensitive data such as passwords are required to be stored in this flow.
* **Fine-Grained Control** — You can control what sort of user interaction you want as a part of the flow, for example a specific hardware device.
* **Better UX** — A user won’t need to remember any passwords or such and will only need to use a hardware authenticator to be able to login to the device.
* **W3C Recommendation** — This means it should be supported by all major browsers across devices.

and lastly **NO MORE PASSWORDS.**

### Disadvantages of WebAuthn

All that being said, it does have some issues which are still to be solved:

* **User Credential Management** — The user experience with respect to credential management is still in a very primitive state.
* **Cross-Device Credentials** — Being able to pass credentials from one device to another is not very easy unless you use a roaming hardware authenticator like a YubiKey.
* **Lost/Stolen Authenticator Device Recovery** — In case you don’t have access or lose your roaming hardware authenticator, the fallback scenario is generally a password to gain access to an account but would need to be explicitly setup.
* **WebAuthn Might Replace Passwords** — WebAuthn is still in a very early phase and is slowly being adopted and supported. It might replace password-based login in the future but it might be a while before we see that happening.

Note — this doesn’t replace things like token-based authentication flows like OAuth or OIDC or identity providers like Auth0, Okta, Google, and others.

## Conclusion

WebAuthn is a much more secure authentication flow than simply using a password. It is phishing resistant and only stores public data on a database with most private data generally stored on the hardware authenticator only. 

It makes use of asymmetric cryptography to do a user check and provides a much better UX compared to the existing login flow.

Currently, WebAuthn is majorly being driven as a two-factor authentication or universal 2nd factor workflow. But it could possibly replace password-based login in the future.

Hopefully, this article helps you understand what WebAuthn is and how it works.

Thanks for reading! I really hope that you find this article useful. I’m always interested to know your thoughts and happy to answer any questions you might have in your mind. If you think this post was useful, please share it so others can see it, too.

Also, do feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/rohitjmathew) or [Twitter](https://twitter.com/iamrohitjmathew).

