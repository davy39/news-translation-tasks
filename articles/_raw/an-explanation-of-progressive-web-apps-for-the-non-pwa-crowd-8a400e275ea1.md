---
title: An explanation of Progressive Web Apps for the non-PWA crowd
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2019-05-13T16:02:17.000Z'
originalURL: https://freecodecamp.org/news/an-explanation-of-progressive-web-apps-for-the-non-pwa-crowd-8a400e275ea1
coverImage: https://cdn-media-1.freecodecamp.org/images/0*bFT4XZ6spjmElUly
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: PWA
  slug: pwa
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: The world of applications was classified into two categories not too long
  ago. You were either creating an application for Android devices or for iOS. Enter
  PWAs, or elongated, Progressive Web Applications. You have probably been hearing
  all about th...
---

The world of applications was classified into two categories not too long ago. You were either creating an application for Android devices or for iOS. Enter PWAs, or elongated, **P**rogressive **W**eb **A**pplications. You have probably been hearing all about them for the past couple of years, but besides a nice acronym, you have no idea what a PWA is. As their popularity increases, it might be a good idea to get to know what all the fuss is about.

In this article, I’ll take you on a tour of what a PWA is, what components it is built from, and show you how you can make one on your own.

#### The Basics

A progressive web application is a website turned into an application. What this means is, that instead of having to code either in Java or Objective-C (or more recent mobile coding languages), you can write the code for the application, like you would for a website. You have your html files, your stylesheets, and your scripts.

Why would you build a PWA instead of a native application? For starters, imagine that once you release a PWA, you can change it constantly without having to republish your application. Since all the code is hosted on a server and not part of the APK/IPA, any change you make happens in real time.

If you have ever used an application that relies on a network connection, you are familiar with the frustration of not being able to do anything. With PWAs, you have the ability to offer an offline experience to your users in case of network issues.

And to add the cherry on top, there is an ability to prompt the user to add your PWA to their home screen. Something that native applications do not possess.

#### Components

There is a standard regarding a PWA, and you must adhere to it if you want to publish one. Each PWA is built from the following components:

* A web app manifest
* A service worker
* Install experience
* HTTPS
* Creating an APK
* Lighthouse audit

#### The Manifest

This is purely a configuration file (**_.JSON_**), enabling you to change various settings of your PWA and how it will appear to the user. Below is an example of one:

You must set either a name/short name key. When setting both, short name will be used on the home screen and the launcher. The name value will be used in the Add to Home Screen experience (or, application install prompt).

Display can have four different values:

* **fullscreen** - this allows your application to take up the whole screen when it is opened
* **standalone** - your application looks like a native application, hiding browser elements
* **minimal-ui** - provides some browsing controls (only supported for Chrome mobile)
* **browser** - like the name says your application’s look will be identical to a browsing experience

You can also set the **orientation** of your application and the **scope** of the pages considered to be within your application.

Don’t forget to add the manifest to your main html file by putting the following meta tag inside of your head tag:

![Image](https://cdn-media-1.freecodecamp.org/images/-sgj8knyKimbaSIeLGhmo5oflTKZzHunce4V)
_Photo by [Unsplash](https://unsplash.com/@solimonster?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">sol</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

#### The Service Worker

A service worker is a component running in the background of your website on the browser. It has a wide set of functionalities including, push notifications, caching assets and providing them for an offline experience and the ability to defer actions until the user has a stable connection to the internet. A service worker can be a whole Medium article on its own, so I won’t delve into the [inner details](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API) of how it works. But, I will supply a vanilla example of one for you to use in your PWA.

It is customary to save the code related to the service worker in a file called **_sw.js_**.

> ✋ The location of the service worker is important since it can only access files that are in the same directory or subdirectory as itself.

A service worker has a lifecycle that can be summed up to the following phases:

* Registration
* Installation/Activation
* Responding to various events

#### Install Experience

One of the unique features of a PWA is its install experience. What this translates to is prompting the user to install your application. To allow us to present this ability to the user, we will need to listen in on an event called **_beforeinstallprompt_**. Below is a code sample demonstrating the flow from presenting the user with the option to add the application to activating logic based on their choice.

![Image](https://cdn-media-1.freecodecamp.org/images/LG4XqHneeagI9dGNOJ28F2oYInSR6vjQRTvy)
_Photo by [Unsplash](https://unsplash.com/@jamessutton_photography?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">James Sutton</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

#### HTTPS

Not too long ago, websites could still use the all too common [http](https://www.w3schools.com/whatis/whatis_http.asp) protocol. Due to recent changes in security and in [Chrome](https://searchengineland.com/effective-july-2018-googles-chrome-browser-will-mark-non-https-sites-as-not-secure-291623), all websites that do not operate under the https protocol will be marked as not secured. Even if your website does not handle user data or sensitive communication, it is still good practice to switch over to https.

And like I mentioned earlier, if you want to be able to release a PWA, it has to use the https protocol. If you don’t want to get into the hassle of acquiring a domain, finding a proper host for it and then enabling SSL, you can go for the easy option of Github. If you have an account, you can open a repository and set up a [GitHub Page](https://pages.github.com/). This process is fairly simple and straightforward and the bonus is getting the HTTPS built in as part of Github.

#### Creating An APK

In order for our PWA to be available inside the Google Play Store, we need to create an APK. You can use the popular tool, [PWA2APK](https://pwa2apk.com/?ref=steemhunt), which will do the hard work for you. But if you prefer to learn how to do it yourself, keep reading.

Google has introduced a new way to integrate your PWA into the Play store using what is called a **_T_**rusted **_W_**eb **_A_**ctivity, or TWA. With just a few simple steps you will learn how to create a TWA, which you can then upload to the Play store.

1. Open Android Studio and create an empty activity
2. Go to the project’s build.gradle file and add the jitpack repository

3. Go to the **_module level_** build.gradle file and add the following lines to enable Java8 compatibility

4. Add the TWA support library as a dependency

5. Add the activity XML inside your AndroidManifest file between the application tags

6. We need to create an association from the application to the website using a digital assets link. Paste the following inside your **_strings.xml_** file

7. Add the next meta tag as a child to your application tag inside the AndroidManifest.xml

8. [Create an upload key and keystore](https://developer.android.com/studio/publish/app-signing#generate-key)

9. Use the following command to extract the SHA-256

10. Go to the [assets link generator](https://developers.google.com/digital-asset-links/tools/generator), supply the SHA-256 fingerprint, the package of your application and the web site's domain

11. Place the result in a file named **_assetlinks.json_** under the location **_/.well-known_** in your website’s directory. Chrome will look for this destination specifically.

12. [Generate a signed APK and upload to the Play store](https://medium.freecodecamp.org/how-to-publish-an-application-in-the-play-store-8ddcc6dc3587)

![Image](https://cdn-media-1.freecodecamp.org/images/mp3eDdZW9F9StMhoajqbVozrN3FPeyDgQw8s)
_Photo by [Unsplash](https://unsplash.com/@aaronburden?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Aaron Burden</a> on <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

#### Lighthouse

By now, I am sure you have already lost track of what is required from your PWA so it will be valid for publishing. There are so many things to take into consideration, that it is easy to lose track of what the requirements are.

Luckily for us, Google has created [Lighthouse](https://developers.google.com/web/tools/lighthouse/#devtools). It can be found in the Chrome Developer Tools (from Chrome version 60). It can be accessed easily by right-clicking inside the browser and selecting inspect. When the new pane opens, you will see an **_Audits_** tab at the far right corner.

![Image](https://cdn-media-1.freecodecamp.org/images/iUXU9aPKpNWuJnHTDj6gfjsMpDewFzo4Zvy4)
_The Audits Tab_

Leaving the settings in this tab as they are, you can now run an audit by clicking on the “Run audits” button. This will take a minute or two, but by the end of it, you will receive an informative, graphical presentation of where your PWA ranks in respect to three properties:

* Performance
* Accessibility
* Best Practices

Each property has a breakdown of where your application passed the requirements and where it didn’t. This lets you see where you need to make adjustments and where you are meeting the standard. If you are interested, you can find a breakdown of the checklist [here](https://developers.google.com/web/progressive-web-apps/checklist#baseline).

#### PWA it up

We are at our journey’s end and hopefully you are feeling better prepared to navigate the world of PWAs. This article was inspired by the process I went through when creating one recently. You can check it out below:

[**Android Menu XML Generator - Apps on Google Play**](https://play.google.com/store/apps/details?id=com.tomerpacific.androidmenugenerator)  
[_Generate any type of menu you need for your Android application. Choose from an Options, Context or Popup menu and…_play.google.com](https://play.google.com/store/apps/details?id=com.tomerpacific.androidmenugenerator)

