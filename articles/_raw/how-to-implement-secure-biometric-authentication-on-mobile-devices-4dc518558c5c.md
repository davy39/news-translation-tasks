---
title: How to implement secure Biometric Authentication on mobile devices
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-17T16:41:09.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-secure-biometric-authentication-on-mobile-devices-4dc518558c5c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XeuEHmQJLOKLRhit-mZZRw.jpeg
tags:
- name: biometric authentication
  slug: biometric-authentication
- name: mobile app development
  slug: mobile-app-development
- name: React Native
  slug: react-native
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Kathy Dinh

  A quick search for React Native biometric authentication would give you several
  tutorials. That was the first thing I did when there was a need for such a feature
  in one of my projects. Depending on the level of risk acceptable for your...'
---

By Kathy Dinh

A quick search for React Native biometric authentication would give you several tutorials. That was the first thing I did when there was a need for such a feature in one of my projects. Depending on the level of risk acceptable for your app, one of those solutions might be suitable. For a high risk app like ours, it would not pass security testing.

If you want to add a secure biometric authentication to aa **_React Native iOS app_**, you are in the right place.

#### **What is wrong with react-native-touchid?**

Most implementations use the _react-native-touchid_ package. At [line 65](https://github.com/naoufal/react-native-touch-id/blob/2e7c4bcd0aedad01e45708fbb831fcc70fc48264/TouchID.m#L65) in the [TouchID.m](https://github.com/naoufal/react-native-touch-id/blob/master/TouchID.m) file, the _authenticate_ method calls the following LAContext method when attempting TouchID/FaceID authentication:

```
evaluatePolicy:localizedReason:reply:^(BOOL success, NSError *error)
```

The method relies on a Local Authentication check if the provided fingerprint matches the one enrolled on the device. When the check passes, a success boolean is returned and the user has authenticated successfully with TouchID/FaceID.

_There have been reports of the possibility to bypass Local Authentication by sending a success signal to Apple’s APIs on jailbroken or non-jailbroken iOS devices_. Thus, biometric authentication via Local Authentication is vulnerable to spoofing by an attacker who could interfere with the check at runtime.

#### **What is the secure way to implement biometric authentication?**

To implement biometric authentication in an iOS app, there are two ways — either through Apple’s Local Authentication APIs or through _access control of Keychain Services_ natively provided by the underlying system.

Authenticating with Local Authentication is simpler but generally not recommended for critical applications. As described in the previous section, Local Authentication is a high level API whose behaviour can be overridden, i.e. an attacker could fake a successful authentication by changing the API’s response.

It is acknowledgedly _best practice to use Keychain Services_ for implementing biometric authentication in high risk apps. Keychain Services enforces access control on its stored content using functionality provided by iOS and [Secure Enclave](https://developer.apple.com/documentation/security/certificate_key_and_trust_services/keys/storing_keys_in_the_secure_enclave). The process executes at the hardware and operating system layer and thus minimises exposure to the less trustworthy application layer. Security risks do exist when user is on a jailbroken or malware-infected device, but these threats can be mitigated by mobile device management (MDM) technology.

#### **How do we implement biometric authentication with Keychain Services?**

In order to access Keychain Services in our React Native app, we are going to use the package [react-native-keychain](https://github.com/oblador/react-native-keychain). The example code is in TypeScript, which should easily be converted to JavaScript.

First, _install_ react-native-keychain and its type declaration as your project dependency:

```
npm i -S react-native-keychain
```

```
npm i -S @types/react-native-keychain
```

Next, we have to _link the library_ as it depends on the native component. There are two ways of linking libraries in a React Native app: automatic linking and manual linking. I encountered many errors with CocoaPods while performing automatic linking. Manual linking works but involves many steps.

I discovered that the library is linked properly without errors if you run _react-native link_ after temporarily removing _Podfile_ under the iOS folder. To save you the hassle, let’s follow such a hybrid approach. Assuming your code is _under version control_ so that it is possible to safely revert any changes, delete your Podfile, _then_ run the linking command:

```
react-native link react-native-keychain
```

Now, undo your Podfile deletion. For iOS 10 you’ll need to enable the `Keychain Sharing` entitlement in the `Capabilities` section of your build target.

![Image](https://cdn-media-1.freecodecamp.org/images/2HiA1V62TFWjNAJW6-sS2E-EpCAkon9aqFjE)

Add the following key value pair to _Info.plist_:

```
<key>NSFaceIDUsageDescription</key><string>Enabling Face ID allows you quick and secure access to your account.</string>
```

Then rebuild your project with:

```
react-native run-ios
```

In case you encounter difficulty in installing react-native-keychain, refer to this [GitHub README](https://github.com/oblador/react-native-keychain).

Before asking the user to authenticate with TouchID/FaceID, it is wise to check if the user’s iOS device supports such capability by calling `[getSupportedBiometryType](https://github.com/oblador/react-native-keychain#getsupportedbiometrytype)`:

![Image](https://cdn-media-1.freecodecamp.org/images/UOLq4S9cQehzR8tgQIJqHEOofr-PK9J4a4lN)

After confirming that biometric authentication is supported, you need to save some content in the keychain and set access control flags. The content could be user credentials or some access token. Keychain entry is encrypted and stored in secure storage. To store a value in the keychain, call `[setGenericPassword](https://github.com/oblador/react-native-keychain#setgenericpasswordusername-password--accesscontrol-accessible-accessgroup-service-securitylevel-)` :

![Image](https://cdn-media-1.freecodecamp.org/images/9tIdxr-QPhcRBF2KOEA7k1stwcsB2RZ21HD-)

A few points to note here:

* Setting _accessControl_ to any of these `[Keychain.ACCESS_CONTROL](https://github.com/oblador/react-native-keychain#keychainaccess_control-enum)` enum values `BIOMETRY_ANY` , `BIOMETRY_CURRENT_SET` , `BIOMETRY_ANY_OR_DEVICE_PASSCODE` , `BIOMETRY_CURRENT_SET_OR_DEVICE_PASSCODE` mandates that the user authenticate with TouchID/FaceID whenever we attempt to retrieve the keychain item.
* We also set _accessible_ to `Keychain.ACCESSIBLE` enum value `WHEN_PASSCODE_SET_THIS_DEVICE_ONLY` . This is the strictest accessible constraint, which enforces:

```
Your device must be unlocked for the secret to be accessible.
```

```
Your device must have a device passcode set.
```

```
If you turn off your device passcode, the secret is deleted.
```

```
The secret cannot be restored to a different device.
```

```
The secret is not included in iCloud backups.
```

Finally, we trigger the TouchID/FaceID authentication prompt by attempting to access the previously stored keychain value with `[getGenericPassword](https://github.com/oblador/react-native-keychain#getgenericpassword-authenticationprompt-service-)` :

![Image](https://cdn-media-1.freecodecamp.org/images/ZX3bMhpsIXH9XNWGJklGOL5yUxNlOrXPkbK6)

Since we saved our secret with access control previously, accessing the item requires user to pass biometric authentication. When authentication is successful, the result returns an object, whose _username_ is ‘your-secret-name’, _password_ is ‘your-secret-value’, and _service_ is ‘your-service-name’.

After _5 failed attempts of TouchID/FaceID authentication system-wide_, biometric authentication is turned off everywhere on the device. The user must lock and unlock the device with a passcode to re-enable TouchID/FaceID. That’s why at line 14 we have to check for supported biometry type and handle the case appropriately, e.g. asking the user to login with their username/password.

#### **Caveats**

Though biometric authentication with react-native-keychain is suitable for critical applications, there are a few caveats I would like to bring to your attention:

**There is _no passcode fallback_**_._ You may receive a requirement to allow the user to authenticate with their device passcode. Looking at the package’s README, you should find `Keychain.ACCESS_CONTROL` enum keys `DEVICE_PASSCODE` , `BIOMETRY_ANY_OR_DEVICE_PASSCODE` , `BIOMETRY_CURRENT_SET_OR_DEVICE_PASSCODE` .

Unfortunately, setting an access control value when calling `setGenericPassword` to any of those three enum keys do not enable an “Enter Password” fallback. [The issue has been reported on GitHub](https://github.com/oblador/react-native-keychain/issues/182), but there has been no response at the time of publishing this article.

You may think of implementing passcode fallback with a different library. Be aware that your system is only _as secure as your weakest link_. If your passcode fallback implementation executes at the application layer, it is a potential target for a security attack and defeats the purpose of relying on Keychain Services for biometric authentication.

Also**, authenticating with react-native-keychain on Android devices _may not be considered secure_** as there is no equivalence of Keychain Services in Android.

#### Wrapping up

Thank you for reading this far. I hope you’ve found the tutorial useful. One improvement you may want to make is asking the user whether they would like to opt-in for biometric authentication before enabling it in your app. Also, you may add a setting to let the user turn on or off TouchID/FaceID authentication in your app settings page.

#### **References**

* [Why local authentication is not secure](https://www.punchkick.com/blog/2016/03/31/best-practices-of-implementing-touch-id-within-financial-apps)
* [How Keychain Authentication with Touch ID Works](https://docplayer.net/62572307-Keychain-and-authentication-with-touch-id.html)

