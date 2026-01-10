---
title: Uno - One Platform to Rule Them All
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-08T11:00:00.000Z'
originalURL: https://freecodecamp.org/news/uno-platform
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/UnoLogoLargeCut-1.png
tags:
- name: C
  slug: c
- name: mobile app development
  slug: mobile-app-development
seo_title: null
seo_desc: "By Kenzie Whalen\nFirst, we should start off with what Uno is and why you\
  \ should care. \nAs stated on their website, Uno is \"The only platform for building\
  \ native mobile, desktop and WebAssembly apps with C#, XAML from a single codebase.\
  \ Open source an..."
---

By Kenzie Whalen

First, we should start off with what Uno is and why you should care. 

As stated on their [website](https://platform.uno), Uno is "The only platform for building native mobile, desktop and WebAssembly apps with C#, XAML from a single codebase. Open source and professionally supported." 

## What does this mean?

Well if you have any experience (or not) building a mobile app and a subsequent web app, you have essentially had to build both separately, outside of potentially sharing data through an API. 

Before Xamarin, you would even have had to build the iOS and Android apps separately using different languages (Swift/Objective-C and Java/Kotlin respectively). Uno introduces a way to build for iOS, Android, Web, and UWP using shared logic and UI. 

This is huge.

Sharing logic between platforms has been the "easy" part for developers. Sharing UI, however, is not. There is a huge difference in UI between Android and iOS and even larger differences between web and mobile. Xamarin.Forms allows us to share UI for Android and iOS but we were still on our own for the web. 

Uno enables you to write the UI once, then, using native controls, deploys native UI look and feel to each of your platforms. This means, you write the same code for a button regardless of the platform the button is for, and the user will see the native button for their platform.

## How does it work?

The Uno Platform works differently depending on what you're building. 

The platform specific UI is created by taking the visual tree and rendering into what the platform supports:

**iOS** _-_ UI Kit

**Android** _-_ ViewGroups and Views

**Web** _-_ Native controls

The logic is also deployed differently for each platform.

When building a UWP app, Uno runs on top of, well, UWP and WinUI. When building Android and iOS apps, Uno runs on top of the Xamarin Native Stack. Finally, when you're building a Web App, Uno runs on top of WebAssembly. The mobile apps and web apps all run with Mono runtime. When it all comes together, it looks a little like this: 

![Image](https://www.freecodecamp.org/news/content/images/2019/09/unodiagram.png)
_High level Uno Platform architecture_

Well this looks nice, but what's really happening under the hood?

## Let's break it down:

**Android and iOS**

1. You write your C# and XAML code in Visual Studio
2. Uno takes the code and lets you add any Xamarin specific libraries or tools 
3. Mono runtime executes the C# code 

This process is essentially the same as regular Xamarin. The big difference between Xamarin and Uno comes with the ability to run the same UI on the Web.

**Web Apps** - 

1. You reuse both your **logic** and **UI**  that you wrote for your mobile apps.
2. Uno uses the _Web Assembly Bootstrapper_ to take any .NET standard library and execute these files in the JavaScript console. 
3. Mono runtime then executes the code 

The ability for Uno to utilize Web Assembly (which is what allows you to write your code in C# and not JavaScript) is what makes Uno so unique. 

**UWP** -

1. You reuse both your **logic** and **UI**  that you wrote for your mobile apps and Web Assembly Apps.
2. Your code is run through the Windows UI which does not need the Mono runtime to execute.

The big difference here is that UWP apps already have the Windows namespaces and do not need to reference the Uno.UI. The benefit Uno provides here is the ability to reuse the code you've already written for mobile and web.

Now that we have an idea of how this beauty works, let's write some code!

To get started with Uno, follow their instructions [here](https://platform.uno/docs/articles/get-started.html).

When you create your Uno solution in Visual Studio, there is a similar feel to when you create a Xamarin.Forms solution because of the different projects created for you. Here is a look at the projects that are auto-created:

![Image](https://www.freecodecamp.org/news/content/images/2019/10/2019-10-01_1528.png)

As you would see in a Xamarin.Forms project, there are separate projects for each platform and a single shared project. The Droid, iOS, UWP, and Wasm projects are all the same as if you had created a blank app for each, the only difference being references to the Uno UI. The magic happens in the _Shared_ project.

Similar to the _Shared_ project in Xamarin.Forms, this is where you will write all your shared logic and UI. Uno provides support for the [MVVM](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93viewmodel), a design pattern many developers are familiar and comfortable with. 

## So, what does a finished product look like?

Using the example "Todo" app provided by Uno [here](https://github.com/unoplatform/workshops/blob/master/uno-bootcamp/modules/99-Ship-your-app/TodoApp.sln), here are examples from each of the four platforms.

iOS

![Image](https://www.freecodecamp.org/news/content/images/2019/10/iOS.png)

Android

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Android.png)

Web

![Image](https://www.freecodecamp.org/news/content/images/2019/10/WASM-1.png)

UWP

![Image](https://www.freecodecamp.org/news/content/images/2019/10/UWP.png)

These projects all use logic and UI from the shared project. Code once, four apps. 

## Let's talk debugging. 

Debugging in Uno can be a bit different depending which platform you are trying to debug. 

**Android and iOS** - For mobile, you will use the same Mono debugger you are used to using in Visual Studio, with access to all your favorite breakpoints, value changes, etc. 

**Web** - Currently there is only support for chromium debugging, which means Chrome and Edge.

**UWP** - Here, the tooling comes from .NET studios which is not as efficient with the mono runtime. 

**Want to try out Uno but don't want to go through the steps to get set up through Visual Studio?** 

Then checkout their [playground](https://playground.platform.uno/#wasm-start)!

![Image](https://www.freecodecamp.org/news/content/images/2019/10/2019-10-02_1518.png)

The Uno Playground is a fun and easy way to look at how different items render on different platforms. They make it quick and easy to try out new styles and is great for beginners and tutorials.

## What are future features we can look forward to?

1. Support for MacOS or Linux.
2. More features from UWP API
3. Support for smart watches

The true beauty of Uno is that it encompasses what we as developers should all be striving to accomplish - building on top of each others' accomplishments. We don't need to re-create the wheel, real innovation happens when you stand on the shoulders of giants and we all move upwards. 

Happy coding. 

For more lessons and tips for Uno, checkout my [blog](https://knzwhalen.com).

