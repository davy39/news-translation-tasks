---
title: How to Set Up Your App for iOS 13 Dark Mode
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-27T13:05:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-an-app-for-dark-mode-on-ios-13-untitled
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/app-developer.jpg
tags:
- name: app development
  slug: app-development
- name: Apple
  slug: apple
- name: iOS
  slug: ios
- name: ios app development
  slug: ios-app-development
seo_title: null
seo_desc: "By Shifa Martin\nApple launched the much-awaited iOS 13 updates globally\
  \ on September 19 across all iPhones launched within the past 4 years (back to the\
  \ iPhone 6s). \n\nOne of the biggest features of this update was the system-wide\
  \ iOS 13 dark mode. It..."
---

By Shifa Martin

Apple launched the much-awaited iOS 13 updates globally on September 19 across all iPhones launched within the past 4 years (back to the iPhone 6s). 

> One of the biggest features of this update was the system-wide iOS 13 dark mode. It's expected to help with eye-strain caused by white light emitted by smartphone displays.

While this feature is a joy to end-consumers using Apple devices, it's a task for iOS developers to prepare an app ready for iOS 13 dark mode.

## How to Set up your App for iOS 13 Dark Mode?

To help developers with this issue, here is useful info and steps showing how they can prep up an existing iOS app for [iOS 13](https://www.apple.com/ae/ios/ios-13/) dark mode.

* It’s not too hard to implement iOS 13 dark mode despite its system-wide scale.
* Enabling iOS 13 dark mode on your existing app is also simple mostly thanks to the latest iOS 13 SDK. 

When using the latest version to build apps for iOS 13 dark mode, the OS will automatically update switches, buttons, and table views among other system controls. Though do note that images and text colors won’t adjust for dark mode automatically.

However, it’s still amazing to see that a system-wide change such as dark mode is so easy to implement. There are smaller code changes and more work that you'll be able to get done with the iOS 13 dark mode in that saved time.

## How to Adapt Colors For iOS 13 Dark Mode

First, let’s start with changing system colors iOS 13 dark mode:

Now there are new system colors added in UIColor, one of which is a label color. Using these new colors helps support dark mode and other high contrast modes in iOS 13.

```js
label.color = UIColor.secondaryLabel
```

Generally, you should use system colors for iOS 13 dark mode, which automatically adapts to changes in the interface for maintaining consistency across apps. However, developers can also choose to implement dark mode with custom colors. 

> The asset catalog colors introduced with iOS 11 make it much easier to support dark mode by adding dark versions of a custom set of colors. 

You only have to select a preferred color from the catalog, then change Appearances to Any, Dark from the Attributes Inspector. 

That's it! Now you have a custom iOS 13 dark mode ready for your mobile app.

## Troubleshooting iOS 13 Dark Mode 

Let's say your app is not following iOS 13 dark mode. What will you do? Here are some easy steps to solve this issue.

### Step 1

You will need to know if the app is updated or not. 

If the app is not working with iOS 13 Dark Mode or does not support it, simply update the app via Apple Store.

### Step 2 

Check whether the Dark Mode of your iOS app has been enabled or not. 

If not, go to Settings - Display & Brightness - check whether "Dark" is enabled or not.

### Step 3  

If your app is fully updated, but isn't working with iOS 13 Dark Mode, then check the in-app settings. _See the image:_

![Image](https://www.freecodecamp.org/news/content/images/2019/09/app-not-following-ios-13s-dark-mode-check-these-settings.w1456-3.jpg)

If you want more help on setting up your iOS 13 Dark Mode, get it from the [dedicated development teams](https://www.valuecoders.com/dedicated-development-teams). And, that is how I'm going to help you. 

Also read tips for [mobile app development on iOS](https://www.valuecoders.com/blog/technology-and-apps/11-tips-successful-mobile-app-development-businesses-android-ios/). Hope all this information will be helpful for you. 

_Let's see what you have to do next._

## Adapt Images For iOS 13 Dark Mode

Most images look great in iOS 13 dark mode, and at times they pop out in a way that really highlights details. However, you may still end up finding some images which look a bit off or unsuitable for dark mode. 

> The good news is that you can adjust images for dark mode in the same way text is adjusted. 

All you need to do is select the image in the catalog and as done previously, and change attributes to Any, Dark in the Attributes Inspector. Now add the dark appearance of the image and we’re done.

## Programmatically Detecting Changes in iOS 13 Dark Mode

Developers could face situations where they need to implement appearance changes in iOS 13 dark mode programmatically. This is how it's done:

```js
override func traitCollectionDidChange(_ previousTraitCollection: UITraitCollection?) 
{
    super.traitCollectionDidChange(previousTraitCollection)

    let userInterfaceStyle = traitCollection.userInterfaceStyle // Either .unspecified, .light, or .dark
    // Update your user interface based on the appearance
}
```

> Overriding traitCollectionDidChange helps in detecting appearance changes.

> Then we only have to open traitCollection.userInterfaceStyle.

**You can also verify if the existing appearance is using a new method you just implemented:**

```js
override func traitCollectionDidChange(_ previousTraitCollection: UITraitCollection?) {
    super.traitCollectionDidChange(previousTraitCollection)

    let hasUserInterfaceStyleChanged = previousTraitCollection.hasDifferentColorAppearance(comparedTo: traitCollection) // Bool
    // Update your user interface based on the appearance
}
```

## Overriding the User Interface Style

### Complete App

The system automatically opts-in any app linked against the iOS 13.0 or later SDK to both light and dark appearances. 

If you need extra time to work on your app’s Dark Mode support or want to keep your app in a single style, you can opt-out by including the UIUserInterfaceStyle key (with a value of Light or Dark) in your app’s Info.plist file. 

Setting this key causes the system to ignore the user’s preference and always apply the specific appearance to your app.

> **Note:** Supporting iOS 13 Dark Mode is strongly encouraged. Use the UI UserInterfaceStyle key to opt-out only temporarily while you work on improvements to your app’s Dark Mode support.

### Specific Screens

In iOS 13, you can now override the user interface style on specific views or view controllers. For example, you may want only a certain view controller to be in iOS 13 dark mode, while the rest of your app is in light mode.

To override the user interface style, just override this variable in the top view or view controller and it will propagate down to sub-views:

```js
// Inside a UIViewController
override func viewDidLoad() 
{
    super.viewDidLoad()

    // Always adopt a dark interface style.    
    overrideUserInterfaceStyle = .dark
}
```

### Closing Notes

Thanks for reading the article! Here we've explored how to set up an app for iOS 13 dark mode. 

iOS 13 dark mode brings with it a unique stress-free way to use a smartphone. Perhaps we’ll see a future where dark mode replaces the default mode with the whiter backgrounds. 

By following these coding guidelines and tips you can easily set up your app for dark mode on iOS 13. 

**If you need some expert help, feel free to g[et in touch](https://www.valuecoders.com/contact) with [iOS developers](https://www.valuecoders.com/hire-developers/hire-ios-developers) for iOS 13 dark mode related queries.**   

**F**ollow on Twitter for** more **updates:** **[https://twitter.com/ValueCoders](https://twitter.com/ValueCoders)****  


  

