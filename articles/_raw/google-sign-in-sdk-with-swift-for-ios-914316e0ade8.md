---
title: How to set up Google Sign In SDK with Swift for iOS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-07-08T07:34:35.000Z'
originalURL: https://freecodecamp.org/news/google-sign-in-sdk-with-swift-for-ios-914316e0ade8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5rAHwA7P4HkBR9S2Gc7e4w.png
tags:
- name: Google
  slug: google
- name: mobile app development
  slug: mobile-app-development
- name: software development
  slug: software-development
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Onur Tuna

  This post is a clearer explanation of the implementation presented in the Google
  Developer tutorial. The Google tutorial recommends you to use pod, however, I don’t
  like to use pod — I want more freedom. So, this tutorial installs and se...'
---

By Onur Tuna

This post is a clearer explanation of the implementation presented in the [Google Developer tutorial](https://developers.google.com/identity/sign-in/ios/start). The Google tutorial recommends you to use pod, however, I don’t like to use pod — I want more freedom. So, this tutorial installs and sets the SDK manually.

The Google tutorial wrote their sample project in Objective-C. At the end of this post, you can find a sample project written in Swift.

#### **Let’s start**

Now we’re going to install the latest SDK from the [Google Developers](https://developers.google.com/identity/sign-in/ios/sdk/) page. Here in this tutorial, the SDK version is 4.0.1. You can use any version but I recommend using the latest one.

When you download the SDK you’re going to see the following files and folders:

* CHANGELOG.md
* GoogleAppUtilities.framework
* GoogleSignIn.bundle
* GoogleSignIn.framework
* GoogleSignInDependencies.framework
* GoogleSymbolUtilities.framework
* README.md
* Sample: This is a sample project written in Objective-C.

Now create a project using Xcode. We’re going to link all necessary frameworks to it. Put the frameworks located in the SDK folder anywhere you want. I prefer collecting all the libraries in a folder called _Library_ under my main _Projects_ folder.

Open your project and go to _Build Settings_. Enter the path where your frameworks are located.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HH3_B3TbZkv1e11e9GvgkA.png)

Next copy the GoogleSignIn.bundle file by drag-dropping into the project. You have to drag and drop the frameworks too but do not copy them.

![Image](https://cdn-media-1.freecodecamp.org/images/1*d_l_eX7V4mZJDTbGtsGL1A.gif)

We need two more frameworks: _Safari Services_ and _System Configuration_. Apple provides them. You can link them in the _Build Phases > Link Binary with Librar_ies.

![Image](https://cdn-media-1.freecodecamp.org/images/1*iTZekslyv8-UM04rmapsvw.jpeg)

The last thing you should do in this part is to add a linker flag. Add the flag below in _Build Settings_ &g_t; Other Linker Fl_ags:

> _$(OTHER_LDFLAGS) -ObjC_

#### **Configuration File**

It’s time for getting a configuration file for your project. You should start an app in the Google Developer page. However, you’ll not copy the configuration file. Instead, keep it anywhere — some information in it might be needed later.

Enter the [page](https://developers.google.com/mobile/add?platform=ios&cntapi=signin&cnturl=https:%2F%2Fdevelopers.google.com%2Fidentity%2Fsign-in%2Fios%2Fsign-in%3Fconfigured%3Dtrue&cntlbl=Continue%20Adding%20Sign-In) to create a project.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mHBTHeMtK7FDdCuBATF_mQ.png)

Choose an app name and give your bundle identifier which you can find under _General_ in Xcode. In the next page, you’ll enable sign in for your app by clicking the _Enable Sign In_ button. After all that, download the _GoogleService-Info.plist_ file. Keep it anywhere you want.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ajc6yD2HOS91ASPdndmMHg.png)

Go back to your Xcode project. Find your reversed client id in the plist file you have just downloaded. Paste it to the _Info > URL Typ_es.

![Image](https://cdn-media-1.freecodecamp.org/images/1*34A0vm7Cf4k-YccveODqbQ.png)

#### **Add Google sign in to app**

Google Sign In SDK is an Objective-C library so you need a bridging header in order to bind it to your Swift project. You can create a bridging header manually. However, you can also leave it Xcode do this automatically.

Create a new .m file with a dummy name. It will ask you to create a bridging header — say yes. Remove the .m file, you don’t need it. Import the Google Sign In in your bridging header.

> #import “GoogleSignIn/GoogleSignIn.h”

Now, go to you app delegate file named _AppDelegate.swift_. Your app delegate should look like something like this.

It seems like a lot of code. However most of it is written by default when you create a new project.

Let me explain the changes. Your class — AppDelegate — now implements _GIDSignInDelegate_ protocol. In order to conform the delegate we have implemented some methods: _application:openURL:options:_ and _signIn:signIn:didSignInForUser:withError:_. Also we have configured GIDSignIn object in the _application:didFinishLaunchingWithOptions:_ method. The rest is not important.

One significant issue is that you should paste your client id in the _application:didFinishLaunchingWithOptions:_ method. You can find your client id in the _plist_ file we downloaded.

#### **Sign in button**

We can add a button and watch our app working. Go to your _ViewController.swift_. The final code should look something like below:

Only one line of code has been added. However, pay attention that our class implements the _GIDSignInUIDelegate_ protocol. We need a button to make the user click. Go to your Story board and put a view on it. Drag and drop a _UIView_. Set _GIDSignInButton_ as the base class and you’re done.

Now run the app and login. You’re finished with the basics. You can use Google Login in your apps from now on. In case you have any problems do not hesitate to contact me.

**Example Codes**

[**onurtuna/Google-Signin-Example**](https://github.com/onurtuna/Google-Signin-Example)  
[_Google-Signin-Example - Google Sign in example using Swift 3_github.com](https://github.com/onurtuna/Google-Signin-Example)

