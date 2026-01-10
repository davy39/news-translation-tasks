---
title: 'Developer Checklist: What should you not miss from WWDC 2019?'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-30T03:50:31.000Z'
originalURL: https://freecodecamp.org/news/developer-checklist-what-should-you-not-miss-from-wwdc-2019
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/danielle-macinnes-222441-unsplash.jpg
tags:
- name: iOS
  slug: ios
- name: ios app development
  slug: ios-app-development
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: technology
  slug: technology
- name: wwdc
  slug: wwdc
seo_title: null
seo_desc: 'By Boudhayan Biswas

  So it’s almost near about one month already since WWDC 2019 happened this year.
  All the developers are still busy what are new things Apple has added or updated
  for development. There were some big announcements and small announce...'
---

By Boudhayan Biswas

So it’s almost near about one month already since WWDC 2019 happened this year. All the developers are still busy what are new things Apple has added or updated for development. There were some big announcements and small announcements, but we, the developers need to make sure that we won’t miss anything important. So I am just creating a quick checklist of the items what we should not miss. Let’s make it short, concise and simple.

### iOS:

1. iOS 13 will let you limit application location access to just once. Until now, there were three options — “Always”, “While Using” or “Never”. One more option has been added to this list “Just Once”. For the first time, you can share your location to an app — just once — and then require it to ask you again next time it wants.
2. Might be one of the popular announcements and people are going crazy about this. Yes, I am talking about “Apple Sign-in”. So it is a requirement from Apple that app developers must implement the company’s new single sign-in solution if the app already offers another third party sign in.
3. You can dismiss modal view controllers interactively which may break some of the existing applications. On iOS 13, by default, the user can just swipe the modal down to dismiss it. So when you are developing a new application make sure to take this into consideration. You can disable this behaviour by `_isModalRepresentation = false_`.
4. `UISegmentedControl` and `UIStepper` are different in iOS 13 with a whole new updated design.
5. A new update to `Localization` in iOS 13. From now, the user can set a different language to each of the application installed in your device. Developers have nothing to change or consider regarding the development, `Settings` application will take care on behalf of you.
6. iOS 13 has almost 1500 different system icons and `UIImage` got a new initializer `UIImage(systemName: )` with this you can now initialize any of the system icons.
7. Until now when you download something in Safari that directly goes into `downloads` folder, but this year Safari got an update and you can change the default download folder to any other folder you want, even you can choose USB drive also.
8. Improvements to `UIStoryboardSegue`. Apple has introduced a new `IBSegueAction` modifier. Now you can pass additional context and parameters directly to the destination view controller that should be initialized.
9. Your apps can provide reservation information to Siri with context and at specific times so the user can take relevant actions based on the circumstances. For example, they can confirm a hotel reservation, be reminded to check in for a flight and get help returning a rental car.
10. With Core NFC framework, your apps can now support tag writing, including writing to NDEF formatted tags. The framework also provides support for reading and writing tags using native protocols such as ISO 7816, MIFARE, ISO 15693, and FeliCa.
11. Synch your Core Data store with CloudKit, giving users of your app seamless access to their data across all their devices. Core Data with CloudKit combines the benefits of local persistence with cloud backup and distribution.
12. Metal gives the GPU even greater control of the graphics and compute pipeline, adds features that make it easier to perform advanced GPU processing, and simplifies the work you need to do to support different kinds of GPUs. New tools, including Metal support in Simulator, help you get started faster and understand whether your iOS app is using Metal correctly.
13. With the new VisionKit framework, your app can let users scan documents using the device’s camera, like those you capture in the Notes app. Combine this feature with Vision’s text recognition to extract text from scanned documents.
14. Core ML 3 now supports on-device model personalization, allowing you to update a model by retraining or fine-tuning it with user-specific data privately from within your app. Core ML has also greatly expanded its support for dynamic neural networks with over 100 layer types.
15. The new PencilKit framework makes it easy to incorporate hand-drawn content into your app quickly and easily. PencilKit provides a drawing environment for your iOS app that takes input from Apple Pencil, or the user’s finger, and turns it into high-quality images you display in either iOS or macOS. The environment comes with tools for creating, erasing, and selecting lines.
16. MetricKit is a new framework that gives you on-device power and performance metrics about your app captured by the system, which you can use to improve the performance of your app.
17. The new Core Haptics framework that lets you compose and play haptic patterns to customize your app’s haptic feedback.
18. Use the new Apple CryptoKit framework to perform common cryptographic operations securely and efficiently, such as Computing and comparing cryptographically secure digests, Using public-key cryptography to create and evaluate digital signatures, Generating symmetric keys, and using them in other operations like message authentication and encryption.
19. Combine is a new framework that provides a declarative Swift API for processing values over time. These values can represent user interface events, network responses, scheduled events, and many other kinds of asynchronous data. With Combine, you declare publishers that expose values that can change and subscribers that receive those values from the publishers. Combine makes your code easier to read and maintain, by centralizing your event-processing code and eliminating troublesome techniques like nested closures and convention-based callbacks.
20. Keep your app content up-to-date and perform long-running tasks while your app is in the background using the new BackgroundTasks framework.
21. RealityKit is a new Swift framework to simulate and render 3D content for use in your augmented reality apps including the ability to add animation, physics, and spatial audio to your AR experience. RealityKit leverages information provided by ARKit to seamlessly integrate virtual objects into the real world.
22. Symbol images give you a consistent set of icons to use in your app, and ensure that those icons adapt to different sizes and to app-specific content. Symbol images use the SVG format to implement vector-based shapes that scale without losing their sharpness. They also support many traits typically associated with the text, such as weight and baseline alignment.
23. With iOS 13, the user can create and manage multiple instances of your app’s user interface simultaneously and switch between them using the app switcher. On iPad, the user can also display multiple instances of your app side by side. Each instance of your UI displays different content or displays content in a different way. For example, the Calendar app can display the appointments for a specific day and for an entire month side by side.
24. SwiftUI is a modern approach to building user interfaces for iOS, macOS, watchOS, and tvOS. You can build dynamic interfaces faster than ever before, using declarative, composition-based programming. The framework provides views, controls, and layout structures for declaring your app’s user interface. It also provides event handlers for delivering taps, gestures, and other types of input to your app, and tools to manage the flow of data from your app’s models down to the views and controls that users will see and interact with.
25. When the Voice Control Accessibility feature is turned on, there’s a blue microphone icon at the top of the device to indicate that the iOS device is in Voice Control mode. The dimmed icon when the phone doesn’t have your attention.
26. One of the new features in iOS 13 is an option in the Files app to connect to the server using SMB. This feature wasn’t working in the first beta but is functional in beta 2, so iOS 13 users can do things like connecting to a home NAS.
27. When sharing a webpage from the Safari Share Sheet, there are new options to share it as a PDF or a Web Archive. There’s also an “Automatic” option that picks the most suitable format for each app or action.
28. No more spam callers. iOS 13 now supports strictly silencing unknown callers.
29. In iOS 13, we got a new method on `UIImageAsset` named `registerImage:withTraitCollection` that can be used to create dynamic images for light and dark programmatically.
30. Running on Low Mobile data? A new “Low Data” mode has been added to avoid running out of data when you’re on a roaming plan.
31. When we do not have wifi then sometimes we face difficulty in downloading apps which are bigger in size. But after iOS 13, we can see a ray of light there. Now the limit has increased to 200 MB, still not enough? Then you can remove the restriction in Settings.
32. Share photo to others with original information in it. iOS 13 is giving you an option to add that original information when sharing.
33. Be happy to mute your iPhone. Apple has introduced a new completely redesigned mute indicator to match Apple pencil charging indicator.
34. Now you can initialize UIViewController subclasses with additional context and arguments (required for dependency injection).
35. If you are not a delegate fan then there are some good news for you. iOS 13 has updated some delegate based APIs to block based API.
36. You do not need to long press on any app and tap on the cross icon to delete. Now you can simply remove an app from AppStore update page by a left swipe.
37. Until now screenshot was taken only in image format. iOS 13 allows you to take a screenshot in pdf format also.
38. iOS 13 has a new `_visualRecursiveDescription` private API that can construct a visual representation of a view hierarchy. Very useful command for debugging in LLDB.
39. A new `UICollectionViewCompositionalLayout` class has been added to UIKit to make it easier to create compositional layouts without requiring a custom `UICollectionViewLayout`.
40. The `UITableViewStyle` enum gained a new public `UITableViewStyleInsetGrouped` case that can be used to create grouped style table views.
41. iOS apps using the File Management APIs can now be granted read/write access to an entire folder, rather than just a file.
42. Tired of swiping in scroll view? In iOS 13, you can drag the scroll indicator to go through a long document.
43. Apps intended for kids cannot include third-party advertising or analytics software and may not transmit data to third parties.
44. MDM provides access to sensitive data, MDM apps must request the mobile device management capability, and may only be offered by commercial enterprises, such as business organizations, educational institutions, or government agencies, and, in limited cases, companies utilizing MDM for parental controls. MDM apps may not sell, use, or disclose to third parties any data for any purpose, and must commit to this in their privacy policy. (referring to apps that abused MDM for Screen Time-like features).

Yeah, it’s quite a long list fully filled with new features. Developers can use all of them to make their application better and smoother. Now let’s take a look at the new frameworks that are coming with iOS 13-

### Frameworks:

1. **BackgroundTasks**: Use the BackgroundTasks framework to keep your app content up to date and run tasks requiring minutes to complete while your app is in the background. Longer tasks can optionally require a powered device and network connectivity. Register launch handlers for tasks when the app launches and schedule them as required. The system will launch your app in the background and execute the tasks.
2. **Combine:** The Combine framework provides a declarative Swift API for processing values over time. These values can represent user interface events, network responses, scheduled events, and many other kinds of asynchronous data. Combine declares _publishers_ to expose values that can change over time, and _subscribers_ to receive those values from the publishers.
3. **CoreAudioTypes:** The CoreAudioTypes framework declares common data types and constants used by other Core Audio interfaces. This framework also includes a handful of convenience functions.
4. **Core Haptics:** Core Haptics lets you add customized haptic and audio feedback to your app. Use haptics to engage users physically, with tactile and audio feedback that gets attention and reinforces actions. Some system-provided interface elements — like pickers, switches, and sliders — automatically provide haptic feedback as users interact with them. With Core Haptics, you extend this functionality by composing and combining haptics beyond the default patterns.
5. **QuickLookThumbnailing**: You may want to create a miniature representation, or _thumbnail_, of a file and its contents to display within your app, or to provide a thumbnail to the operating system. For example, macOS shows thumbnails as part of the Finder app and its Quick Look feature. The QuickLookThumbnailing framework provides an API to generate thumbnails for common file types using the `QLThumbnailGenerator` object.
6. **PencilKit**: PencilKit makes it easy to incorporate hand-drawn content into your iOS or macOS apps quickly and easily. PencilKit provides a drawing environment for your iOS app that takes input from Apple Pencil, or the user’s finger, and turns it into high-quality images you display in either iOS or macOS. The environment comes with tools for creating, erasing, and selecting lines.
7. **RealityKit**: Use the RealityKit framework to implement high-performance 3D simulation and rendering. RealityKit leverages information provided by the ARKit framework to seamlessly integrate virtual objects into the real world.
8. **VisionKit**: VisionKit is a small framework that lets your app use the system’s document scanner. Present the document camera as a view controller, which covers the entire screen like the camera function in Notes.
9. **SoundAnalysis**: Use the SoundAnalysis framework to analyze audio and recognize it as a particular type, such as laughter or applause. The framework performs its analysis using a Core ML model trained by an `MLSoundClassifier`. Using the framework’s ability to analyze streamed or file-based audio lets you add intelligent audio recognition capabilities to your app.
10. **CryptoKit**: Use Apple CryptoKit to perform common cryptographic operations: Compute and compare cryptographically secure digests. Use public-key cryptography to create and evaluate digital signatures, and to perform the key exchange. In addition to working with keys stored in memory, you can also use private keys stored in and managed by the Secure Enclave. Generate symmetric keys, and use them in operations like message authentication and encryption. Prefer CryptoKit over lower-level interfaces. CryptoKit frees your app from managing raw pointers, and automatically handles tasks that make your app more secure, like overwriting sensitive data during memory deallocation.
11. **Maps Web Snapshots**: The Maps Web Snapshots service can be used to generate static map images from a URL. You can use Snapshots any time that an interactive map is not required, and in any place, you typically use an image URL — in web pages, and in places where JavaScript is not available, such as email clients.
12. **DriverKit**: Use DriverKit to create device drivers that the user installs on their Mac. Drivers built with DriverKit run in userspace, rather than as kernel extensions, for improved system security and stability.
13. **MetricKit**: With MetricKit, you can receive on-device app power and performance metrics captured by the system. A registered app receives reports containing data about the previous 24 hours at most once per day. Use the data in the reports to help improve the performance of your app.
14. **SystemExtensions**: Creating system extensions allow your app to enhance the capabilities of the user’s Mac, without the associated risks of developing kernel extensions (KEXTs). System extensions run in userspace, where they can’t compromise the security or stability of macOS. The system grants these extensions a high level of privilege, so they can perform the kinds of tasks previously reserved to KEXTs.
15. **EndpointSecurity**: Use the Endpoint Security library to create security-related software. Endpoint Security clients monitor system events for potentially malicious activity. Your client registers with Endpoint Security to authorize pending events, or receive notifications of events that have already occurred. These events include process executions, mounting file systems, forking processes, and raising signals.
16. **USBSerialDriverKit**: The USBSerialDriverKit framework provides an API for developing serial communication drivers for USB devices like modems and serial adapters. The framework builds on DriverKit by adding the ability to set attributes like baud rate and parity and work with a device’s universal asynchronous receiver/transmitter (UART).
17. **USBDriverKit**: Use the USBDriverKit framework to develop drivers for custom or non-class compliant USB devices for use with macOS. USBDriverKit provides C++ classes you can use to attach and configure your device and create USB message and stream pipes to exchange data. USBDriverKit devices work with the core types defined in the DriverKit framework.
18. **HIDDriverKit**: The HIDDriverKit framework provides C++ classes for developing drivers for human interface devices: keyboards, pointing devices, and digitizers like pens and touchpads. HIDDriverKit uses the core types defined in DriverKit, and adds features specific to human interface device development.

That’s all for today. Happy coding!!

**_???Thank you for reading???_**

