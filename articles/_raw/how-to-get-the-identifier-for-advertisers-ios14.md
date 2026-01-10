---
title: How to Get the Identifier For Advertisers (IDFA) in iOS14
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2020-09-22T17:44:12.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-the-identifier-for-advertisers-ios14
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/0_oIyg9OzrsA2PiXHW.jpg
tags:
- name: Apple
  slug: apple
- name: iOS
  slug: ios
- name: ios app development
  slug: ios-app-development
- name: mobile app development
  slug: mobile-app-development
seo_title: null
seo_desc: "If the title of this article means something to you, then you are probably\
  \ aware of the earthquake caused by iOS14. \nWith the release of iOS14, there have\
  \ been major changes in the way applications can gather information about a user.\
  \ One of them dea..."
---

If the title of this article means something to you, then you are probably aware of the earthquake caused by iOS14. 

With the release of iOS14, there have been major changes in the way applications can gather information about a user. One of them deals with the Identifier For Advertisers (or IDFA) and how applications can access it. 

But for those that don't know, let's first explain what the IDFA is and why it's important.

## What is an IDFA?

Each iOS device owner can decide whether they want to be tracked by advertising companies. This allows those companies to supplying that user with content that is tailored towards them (based on their online browsing habits).

Companies can do this with what’s known as an IDFA (Identifier For Advertisers). This is a [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#:~:text=A%20universally%20unique%20identifier%20(UUID,%2C%20for%20practical%20purposes%2C%20unique.) string that lets advertisers match the user with their behavior.

Here's an example of a UUID string : 123e4567-e89b-12d3-a456–426614174000.

### So, what are those changes we talked about earlier?

In short, applications will now be required to show a dialog to the user, asking them if they want to allow the application to track them or not.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screen-Shot-2020-09-17-at-22.35.25.png)
_The Tracking Authorization Dialog_

Looks pretty ominous, right?

This is in contrast with how things worked before iOS14, where you only had to check if the device had limited advertising tracking enabled or disabled.

The newest version of Apple’s operating system (iOS14) is already available (has been since September 16th). Developers who use the IDFA have to make changes in their applications in order to be compatible for iOS14. 

On September 3rd, Apple made an [update](https://developer.apple.com/news/?id=hx9s63c5%27) and pushed the deadline to complete these updates to the start of next year:

> “To give developers time to make necessary changes, apps will be required to obtain permission to track users starting early next year”

Now that we have some time to regain our composure and breathe again, let’s start preparing ourselves for what’s going to be the new normal in 2021. 

In this article, we'll present some background about the IDFA and see how we can get its value from iOS14 and onwards.

## How does the IDFA Get Used By Advertisers?

Let’s take a scenario (pre COIVD-19) where you are browsing the web on your iPhone and are looking for a hotel for your next vacation. 

Each ad that you see will send a pixel with your IDFA attached to it. An advertiser can see that you are looking at a lot of ads promoting hotels by matching your IDFA and conclude that you are looking to book a hotel room. 

From there, it won’t be long until you will be shown a lot of ads for hotel rooms.

This simple yet profound technology came into our lives back in 2012 with iOS6. Since then a lot has changed, and iOS14 is flipping the industry on its head, yet again.

_✋_ Note: _To use these new APIs you must have upgraded/downloaded XCode 12_.

## Advertising Tracking And Getting The IDFA

Before iOS14, getting the IDFA was pretty simple.

You had to check whether [Advertising Tracking](https://developer.apple.com/documentation/adsupport/asidentifiermanager/1614148-isadvertisingtrackingenabled) was enabled or not, by doing this:

```[[ASIdentifierManager sharedManager] isAdvertisingTrackingEnabled]```

And if it was disabled, that meant you could acquire the IDFA through the [ASIdentifierManager](https://developer.apple.com/documentation/adsupport/asidentifiermanager) class, like so:

```[[[ASIdentifierManager sharedManager] advertisingIdentifier] UUIDString];```

Simple enough, right?

_☝️ Beginning_ with _iOS10, if the user disabled advertising tracking, the method above would return a UUID string filled with zeros._

One of the changes in iOS14 is the deprecation of the method that checks whether advertiser tracking is enabled or not. So how can applications get the coveted IDFA from iOS14 and onward?

They will have to use a new API that presents a dialog to the user. A few words of wisdom regarding this dialog:

* It can only be presented to the user **once**
* The only thing that can be altered in the dialog’s UI are the two lines above the Allow Tracking option (**“Do you want to be tracked?”**)

This means that developers will need to think long and hard about how and when they will present the message to the user.

## Authorization Status

With iOS14, a new framework has been created called [App Tracking Transparency](https://developer.apple.com/documentation/apptrackingtransparency?language=objc). This framework contains a class called [ATTrackingManager](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager?language=objc), which provides an API to:

1. Present a dialog to the user requesting permission to track them
2. Query the authorization status (regardless of showing or not showing the dialog)

We’ll first learn how to get the authorization status. To do so, you need to call the **trackingAuthorizationStatus** method.

```ATTrackingManagerAuthorizationStatus status = [ATTrackingManager trackingAuthorizationStatus];```

It will return an NSUInteger with one of the following values:

* ATTrackingManagerAuthorizationStatusNotDetermined = 0
* ATTrackingManagerAuthorizationStatusRestricted = 1
* ATTrackingManagerAuthorizationStatusAuthorized = 3
* ATTrackingManagerAuthorizationStatusDenied = 2

The first three results are pretty self explanatory, so we will focus for a minute on the last one. 

You can get an authorization status that is restricted when the screen for enabling/disabling advertising tracking is locked and this option is set to enabled.

Apple has acknowledged this in devices that are identified as belonging to children (for example).

## Asking For Permission To Track

Before looking into the code needed to present the dialog, you must first include the **NSUserTrackingUsageDescription** key inside your info.plist file. 

What you add as the value for this key will appear as the two lines mentioned earlier, in the dialog.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/Screen-Shot-2020-09-17-at-22.29.31.png)
_**NSUserTrackingUsageDescription in the info.plist file**_

To present the dialog, we need to call [requestTrackingAuthorizationWithCompletionHandler](https://developer.apple.com/documentation/apptrackingtransparency/attrackingmanager/3547037-requesttrackingauthorizationwith?language=objc):

```
[ATTrackingManager requestTrackingAuthorizationWithCompletionHandler:^(ATTrackingManagerAuthorizationStatus status) {
        if (status == ATTrackingManagerAuthorizationStatusDenied) {
            //Logic when authorization status is denied
        } else if (status == ATTrackingManagerAuthorizationStatusAuthorized) {
            //Logic when authorization status is authorized
        } else if (status == ATTrackingManagerAuthorizationStatusNotDetermined) {
            //Logic when authorization status is unknown
        }  else if (status == ATTrackingManagerAuthorizationStatusRestricted) {
            //Logic when authorization status is restricted
        }
    }];
```

In the first picture of this article (where you see the dialog) you can see that the lines we wrote in the info.plist file show up as the two lines in the dialog.

## Wrapping up

In conclusion, it's important to remember that these changes, while daunting, are not happening immediately. 

You should also make sure to follow all of the steps detailed in this article so as not to come across crashes/errors in your applications.

