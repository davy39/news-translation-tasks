---
title: How to use Touch ID for a quicker, easier login to your app
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-11T09:37:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-touch-id-for-a-quicker-easier-login-to-your-app-e22356c9ef9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iHa_tmMWld0abbhzTUJcEQ.jpeg
tags:
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Akul Tomar

  It is a common observation that users drop off a little on your login screen. This
  is how I tackle my facebook addiction? . This tutorial teaches you how to utilize
  Touch ID for a faster and easier login. I’ll take you through the steps...'
---

By Akul Tomar

It is a common observation that users drop off a little on your login screen. This is how I tackle my facebook addiction? . This tutorial teaches you how to utilize T**ouch ID** for a faster and easier login. I’ll take you through the steps soon, just let me brief you a little.

Most apps use Touch ID as a second degree authentication. This tutorial is NOT about providing a second degree authentication (although you can do that too if you read this article). It’s about using Touch ID to make that server call to login the user.

Now how do you get the user’s credentials from their thumb print to make that server call? ? This is where K**eychain service c**omes in. When the user signs up or logs into your app for the first time, save the credentials to your app’s keychain. Next time, when the user logs out and then visits the login screen again, flash a popup asking them to login using Touch ID. When the user provides a valid Touch ID, get those user credentials you saved earlier to the keychain, make your API call, and Boom!?.

So there are two steps involved here:

* First, you need to save the user’s credentials to the keychain. You can do this when the user signs up or when they log into your app for the first time.
* Second, use Touch ID to verify the user, then retrieve their credentials from the keychain service.

I’m using **KeychainPasswordItem**, a nice wrapper over Keychain available on developer.apple.com [here](https://developer.apple.com/library/content/samplecode/GenericKeychain/Listings/GenericKeychain_KeychainPasswordItem_swift.html#//apple_ref/doc/uid/DTS40007797-GenericKeychain_KeychainPasswordItem_swift-DontLinkElementID_7). They have a very good, detailed example on how to use this generic keychain. Go have a look.

As part of the first step, use the call method below with the user’s email as account and password when the user signs up and logs in.

We are storing the user’s email to **UserDefaults** to be used later. It would be better if you flash a popup to ask the user’s permission to use this feature. I’m skipping that part for this tutorial?.

#### Use Touch ID to access the keychain

To use Touch ID, you first need to add the LocalAuthentication framework to your project binaries. You can do this by going to Project > Build Phases > Link Binary With Libraries:

![Image](https://cdn-media-1.freecodecamp.org/images/1*1jVJSkOY95UDo9i0FZiXNg.png)

Next, import the LocalAuthentication framework in your login view controller.

```
import LocalAuthentication
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*luSj-qKPFtV5PjvAEZZQrQ.png)

We’ve filled our userName textfield with the user account email we saved earlier to **UserDefaults.**

Next, we need to check whether authentication is possible on the current device. Check out the following code:

We invoke **authenticateUserUsingTouchId**() in **viewDidAppear**(). LAContext is a subclass of NSObject, and represents our current authentication context. Now, if authentication is possible, validate Touch ID’s authenticity by calling evaluatePolicy()

![Image](https://cdn-media-1.freecodecamp.org/images/1*vU1Q2tyhAB0yoTVoEa_a7Q.png)

**context.evaluatePolicy()** gives us the Touch ID popup with our last accessed user name, which we gave as our localizedReason in the **evaluatePolicy() method**.

This completes Part 1 of Step 2: getting the user to authenticate using Touch ID. Next up is using Touch ID to access the Keychain where we save or retrieve user credentials for login.

When the user provides a valid Touch ID, we need to load the password from the Keychain and make our POST call to login the user.

```
if authSuccessful {             self.loadPasswordFromKeychainAndAuthenticateUser(lastAccessedUserName)}
```

That’s it! You can upgrade your authentication framework to support multiple accounts. After verifying Touch ID’s authenticity, flash a popup and ask the user to select the account they wish login. Then retrieve the user’s credentials corresponding to that account from the Keychain. Thanks for reading!

