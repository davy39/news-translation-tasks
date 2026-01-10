---
title: How to use Visual Studio Team Services for iOS native apps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-04-11T09:18:21.000Z'
originalURL: https://freecodecamp.org/news/devops-for-ios-native-apps-with-visual-studio-team-services-1d792ae997f1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Mm3f1tm-X0dpyjNbiubucw.gif
tags:
- name: Continuous Integration
  slug: continuous-integration
- name: Devops
  slug: devops
- name: iOS
  slug: ios
- name: ios app development
  slug: ios-app-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Khawaja Farooq

  Visual Studio Team Services (VSTS) provides an easy way to share code, automate
  builds, run unit tests, and ship software. Developers from a wide range of platforms
  rely on it. It promotes continuous integration, which can accelerat...'
---

By Khawaja Farooq

[Visual Studio Team Services](https://www.visualstudio.com/team-services/) (VSTS) provides an easy way to share code, automate builds, run unit tests, and ship software. Developers from a wide range of platforms rely on it. It promotes continuous integration, which can accelerate the process from concept to delivery.

Microsoft has done a substantial amount of work to improve DevOps for Mobile and other platforms. However, there are no specifics for the iOS native platform. Here’s a guide on how to set up VSTS for an iOS project, so you can leverage its continuous integration capabilities.

Here are the pre-requisites to get started:

1. Buildable Xcode project on GitHub / TFS
2. VSTS Account

### Create a VSTS Project

Create a new team project → _Settings > Overview > New team p_roject

![Image](https://cdn-media-1.freecodecamp.org/images/5A8zGgcE0E9K8mDwFCz5BXOaDQ7vd6SFb0Gl)

The next step is to import your existing repository. For now, we are using GitHub. Click _import a repository_.

![Image](https://cdn-media-1.freecodecamp.org/images/1d1RSYgmeYA-ZfyKTc6G8XYthoZYEw7X5S0w)

Now you have your own copy of the repository that you should be able to see!

### Install the iOS Build Agent

VSTS doesn’t have any preinstalled agent for building an Xcode project. This part is crucial.

Fortunately, the configuration is covered by [James Montemagno for Xamarin iOS](https://blog.xamarin.com/continuous-integration-for-ios-apps-with-visual-studio-team-services/). For convenience, I’m quoting some of the steps here.

You’ll need to install the following items to prepare your Mac:

1. [Homebrew OS X](https://brew.sh/)
2. [.NET Core](https://www.microsoft.com/net/core#macos)
3. Install npm using command: **brew install npm**
4. Create a [Personal Access Token](https://www.visualstudio.com/en-us/docs/setup-admin/team-services/use-personal-access-tokens-to-authenticate) (PAT) and for the scope: _Agent Pools (read, manage)_

#### Agent Queue

1. Create new agent queue “OSX” → _Settings > Agent que_ues
2. Download and configure the build agent for OS X.

![Image](https://cdn-media-1.freecodecamp.org/images/NAUNW7VQqw2hrykcwebAuOGtM2d0vR6LtTPf)

Once the configuration is done, run the build agent with the following command:

```
./run.sh
```

Well done! You have an on-premise build agent running.

### Create the Xcode Build Definition

Once you have installed the build agent, it’s time to create a build definition. These steps will create a build definition for Xcode iOS instead of Xamarin. Go to → _Build & Release > New Definition >_ Xcode

![Image](https://cdn-media-1.freecodecamp.org/images/4LvE4SuRG5N0qxdYKwSQUlhVCi0USraGR6Cr)

Don’t forget to select your agent pool that you just created.

![Image](https://cdn-media-1.freecodecamp.org/images/56A8HwKcOuabTD90G6YtIlANIbjgL8yjOn30)

Xcode build definition may look like the following:

![Image](https://cdn-media-1.freecodecamp.org/images/yvVzVxSGbdcjjCZYdqMq8-2tT5eAM6-LdkWb)

_Workspace path_ varies whether you are using an Xcode workspace or just a project.

In case you are using an Xcode workspace:

```
*.xcodeproj/project.xcworkspace
```

For an Xcode project:

```
*.xcodeproj
```

You can also use some utilities to [copy and publish your build artifacts](https://www.visualstudio.com/en-us/docs/build/steps/utility/copy-and-publish-build-artifacts).

Next, save the build definition and queue a new build…

![Image](https://cdn-media-1.freecodecamp.org/images/2RpYOp-3o9-teatL7pMOdGdQC07Ib0zcgNlf)

You should get a build error. We need to make one change to the Xcode project configuration.

### Configure the Xcode project/workspace

VSTS needs a shared project scheme in order to build the project. Make sure to enable it. _Xcode_ → _Product > Schemes > Manage s_chemes

![Image](https://cdn-media-1.freecodecamp.org/images/KMojWE198TJHgM6B7MB-IIoBfqMy10Lp3taL)

Now push the changes to your source control and build again.

![Image](https://cdn-media-1.freecodecamp.org/images/y0IatW3Lfq-dKdu1xlu0TeYwoMxr57Aray42)

### Deploy to HockeyApp

HockeyApp helps testers for beta app testing. It’s easy to install [the VSTS Extension](https://marketplace.visualstudio.com/items?itemName=ms.hockeyapp) from the marketplace. This enables the app to be uploaded after it builds successfully.

![Image](https://cdn-media-1.freecodecamp.org/images/8F1g9Qo9BhY-YvAPtarq-eBfjwcbNca1ntny)

[**_Download & import sample build definition_**](https://github.com/khawajafarooq/XcodeBuildDefinition)

Visual Studio Team Services provides continuous integration for iOS developers. By automating a lot of repetitious tasks, it saves you time.

Another option is [MacinCloud](http://www.macincloud.com/), a cloud solution for building iOS native apps. For now, we have reviewed on-premise build capabilities as _Azure_ doesn’t provide VM support for Mac OS X. Give VSTS a try and leave any feedback in the comments or get in touch on twitter [@khfarooq](https://twitter.com/khfarooq), that’s what keeps me going. Thanks for reading! ?

