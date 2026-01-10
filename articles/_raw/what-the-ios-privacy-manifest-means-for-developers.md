---
title: What the iOS Privacy Manifest Means for Developers
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2024-03-15T16:56:05.000Z'
originalURL: https://freecodecamp.org/news/what-the-ios-privacy-manifest-means-for-developers
coverImage: https://www.freecodecamp.org/news/content/images/2024/03/pawel-czerwinski-jj4LC7iKA6Q-unsplash.jpg
tags:
- name: privacy
  slug: privacy
seo_title: null
seo_desc: 'At WWDC 2023, Apple introduced us to a new bundle resource that is going
  to be added to every application and library: the privacy manifest. A lot has been
  written since then about this subject but without that much clarity.

  When first announced, App...'
---

[At WWDC 2023](https://developer.apple.com/videos/play/wwdc2023/10060), Apple introduced us to a new bundle resource that is going to be added to every application and library: the privacy manifest. A lot has been written since then about this subject but without that much clarity.

When first announced, Apple stated that in the Spring of 2024 (read – spring is already here), having a privacy manifest is expected and will be part of [the application review process](https://developer.apple.com/distribute/app-review/). Apple also asks application developers, as well as SDK developers, to adopt the privacy manifest.

Fast forward to December 7th, 2023, [Apple announced](https://developer.apple.com/news/?id=r1henawx#:~:text=Third%2Dparty%20SDK%20privacy%20manifest%20and%20signatures.&text=Starting%20in%20spring%202024%2C%20if,used%20as%20a%20binary%20dependency.) a list of “commonly used third-party SDKs” that, if included by your application, you have to have a privacy manifest for. No real explanation has been given as to why the third-party SDKs listed are the ones that have been selected, but there has been much speculation about it.

And here we stand after February 29th, 2024 (on a leap day!), when [Apple announced](https://developer.apple.com/news/?id=3d8a9yyh) a timeline for enforcing the required reason API section of the privacy manifest.

All of this has led to quite a bit of confusion from developers who are scrambling to understand if their application or SDK falls into a privacy manifest category.

Developers are unsure if they should add a privacy manifest to their SDK, even if it is not listed. The [documentation](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files) itself, while being adept at giving an outline of everything, lacks the necessary distinctions and details developers are looking for.

Part of me wants to say that Apple is keeping things vague since the near future has coming changes that privacy manifests will bring. Another part of me says that Apple has always been this vague, and it is just their modus operandi.

In any case, you are reading this article because you want to understand how all of this affects you. So, let’s break things down.

> _⚠️ Disclaimer: This article won’t deal with explaining what the privacy manifest is or how to add it to your application/library, as that has been covered by Apple's documentation fairly well._

## The Four Horsemen

Privacy manifest is divided into four subjects:

* NSPrivacyTracking.
* NSPrivacyTrackingDomains.
* NSPrivacyCollectedDataTypes (nutrition labels).
* NSPrivacyAccessedAPITypes (required reason APIs).

The first two are tied together and can pose the most substantial changes to your application/library, so we’ll ease into this list by starting with number three.

### What are NSPrivacyCollectedDataTypes?

This section holds various categories of data collection that if your application or SDK does something with, you have to declare them. 

Each type of data collected must be supplied with the reason for collecting it. 

The categories range from contact information about the user (such as email/phone number), to Location and Purchases. 

Inside your privacy manifest file, you will have an array of NSPrivacyCollectedDataTypes, where each item will hold:

* The type of data collected.
* Whether or not this data is linked to the user.
* Whether or not this data is used to track the user.
* The reason(s) for collecting this data.

Let’s do one as an example. Imagine your application collects the precise location of a user in order to track the user’s movement to see if the user is nearby any specific stores. 

If the user is nearby such a store, you present a relevant ad to them. Factoring all that you will need to create an entry where:

* The data type will be NSPrivacyCollectedDataTypePreciseLocation.
* Mark true as we are linking the data to the user.
* Mark true as we are tracking the user with this data.
* Since we are going to display ads to the user, we will choose. NSPrivacyCollectedDataTypePurposeThirdPartyAdvertising, NSPrivacyCollectedDataTypePurposeProductPersonalization, and NSPrivacyCollectedDataTypePurposeAppFunctionality since all of those fit for the data we collect.

### What are NSPrivacyAccessedAPITypes?

As mentioned, this section gets a bit more obscure and a bit more demanding.

Here, Apple lists very specific APIs from different categories that if you happen to use, you need to declare them. 

For every API listed, there are specific reasons you need to fall into in order to declare your use of it. Some reasons state clearly that even if you use the API, you cannot send the data received by this API to a server (off-device). 

If you find that your application or SDK uses one of the listed APIs, then you need to list it with an appropriate reason(s). For example, if we use the example from the previous section, our application reads and writes data to user defaults that has to do with the user’s location. So, we will need to:

* List NSPrivacyAccessedAPICategoryUserDefaults as the NSPrivacyAccessedAPIType.
* Use CA92.1 inside the NSPrivacyAccessedAPITypeReasons.

If you think you don’t see the reason you are using an API for, [you can let Apple know about it](https://idmsa.apple.com/IDMSWebAuth/signin.html?path=%2Fcontact%2Frequest%2Fprivacy-manifest-reason%2F&appIdKey=891bd3417a7776362562d2197f89480a8547b108fd934911bcbea0110d07f757&rv=0).

> 🎯 None of the APIs listed can be used for tracking the user.

At last, we come to the two most problematic categories.

### What are the NSPrivacyTracking and NSPrivacyTrackingDomains?

What is tracking? Do you know? Does anyone know? It really doesn’t matter, because [Apple has a definition for it](https://developer.apple.com/app-store/app-privacy-details/#user-tracking):

> _“Tracking” refers to linking data collected from your app about a particular end-user or device, such as a user ID, device ID, or profile, with Third-Party Data for targeted advertising or advertising measurement purposes, or sharing data collected from your app about a particular end-user or device with a data broker._

So, if your application or SDK doesn’t fall into that definition, you need to mark false as the value for NSPrivacyTracking and you can exhale. 

Because if you have to mark true as the NSPrivacyTracking, then you must supply all the domains your application or SDK uses for the purpose of tracking as part of NSPrivacyTrackingDomains.

By now, you must be asking yourself, why I am making a big fuss about this. Well, it has to do with the fact that Apple will block all requests to any domain listed under NSPrivacyTrackingDomains if the user doesn’t allow the application to track him/her.

Read the paragraph above again.

Get it? You will now need to re-route network requests differently based on whether the user has given consent to be tracked or not. 

On the client side (application/library), this might be a small change to handle. But on the server/infrastructure side, this might require some heavy lifting as new domains (or sub domains), need to be created. 

Data that has been aggregating a certain way, now needs to be aggregated from another source. You obviously also need to make sure that no tracking related data is sent to your newly created domains. You wouldn’t want to end up in a scenario where your application/library stops working entirely.

To assist you in understanding which domains fall into the tracking category, you can use [Instruments](https://developer.apple.com/documentation/xcode/detecting-when-your-app-contacts-domains-that-may-be-profiling-users). Be aware that if your domains do not fall into that category now, it doesn’t mean that they won’t fall into it later.

## Conclusion

As with any new regulation or policy, many questions are still left unanswered:

* If my application has a webview, where some network requests are made, do I have to include those as domains for NSPrivacyTrackingDomains?
* Are sub domains good enough or do developers need to create completely different domains?
* If my library is not listed as part of the commonly used SDKs, is there a chance that it might be in the future? What is the criteria used for listing such SDKs?
* Do I have to include a signature to my SDK even if it is not listed under the commonly used SDKs?

Also, when looking at the current state of things in the developer community, the response is quite the same. At the time of writing this article, numerous SDKs that are listed in Apple’s list, still haven’t released a version with a privacy manifest.

As we will get closer to the date of when it will be mandatory to have a privacy manifest, hopefully more details will emerge and better clarity. Until then, brace yourselves.

