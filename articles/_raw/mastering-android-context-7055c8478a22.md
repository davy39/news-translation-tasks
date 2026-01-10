---
title: Mastering Android context
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-05T10:11:45.000Z'
originalURL: https://freecodecamp.org/news/mastering-android-context-7055c8478a22
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5tMVgzhvyHZtlBW48OUsug.jpeg
tags:
- name: Android
  slug: android
- name: Apps
  slug: apps-tag
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Gaurav

  Context in Android is one of the most used and abused objects. But most of the articles
  on the web focus on the definition of what it is. I could not find a good resource
  which gave me insight and helped me understand the bigger picture. So...'
---

By Gaurav

Context in Android is one of the most used and abused objects. But most of the articles on the web focus on the definition of what it is. I could not find a good resource which gave me insight and helped me understand the bigger picture. So I tried simplifying things with this article.

![Image](https://cdn-media-1.freecodecamp.org/images/xYtafNOmFZOHjNUTahCLSVsNkwPP7JSR1gxn)
_Which Context to use? Image Credit: Pexels_

### Preface

My mission for this article is to help you master Android Context. This is one of the core topics of Android development, and hardly any developers use context completely and in the way it was designed.

I originally published this article as a series of four posts on my [website](https://gaurav-khanna.in/). If you are interested in reading chapter by chapter, [feel free to read there](https://gaurav-khanna.in/blogs/android/mastering-android-context/).

### Getting started

Have you ever encountered this question: What is difference between `getContext()`, `this`, `getBaseContext()`, and `getApplicationContext()`? If yes, this article will help clarify most of your confusion.

**Note:** you should know the basics of Android development, like Activity, Fragments, Broadcast Receiver, and other building blocks. If you are a new developer who is just starting your journey into the Android world, this might not be the best place to begin.

### What the heck is context?

Let’s face it, Context is one of the most poorly designed features of the Android API. You could call it the “God” object.

An Android app or application package kit (APK) is a bundle of components. These components are defined in the Manifest, and consist mainly of Activity (UI), Service (Background), BroadcastReceiver (Action), ContentProvider (Data), and Resources (images, strings etc).

The developer can choose to expose those components to a system using an intent-filter. For example: send email or share picture. They can also choose to expose the components only to other components of their app.

Similarly, the Android operating system was also designed to expose components. A few well known are WifiManager, Vibrator, and PackageManager.

Context is the bridge between components. You use it to communicate between components, instantiate components, and access components.

#### **Your own components**

We use context to instantiate our components with Activity, Content Provider, BroadcastReceiver, and so on. We use it to access resources and filesystems as well.

#### **Your component and a system component**

Context acts as an entry point to the Android system. Some well-used System components are WifiManager, Vibrator, and PackageManager. You can access WifiManager using `context.getSystemService(Context.WIFI_SERVICE)`.

In this same way, you can use context to access the filesystem dedicated to your app as a user in OS.

#### **Your own component and some other app’s component**

Communicating between your own components and other app’s components is almost identical if you use the intent-filter approach. After-all, every components is an equal citizen in Android.

An example of an intent used to send email is below. All components which are offering this intent action will be served to the user who can opt what to use.  
 `Intent emailIntent = new Intent(android.content.Intent.ACTION_SEND);`

#### Summary

Let’s agree that everything in Android is a component. Context is the bridge between components. You use it to communicate between components, instantiate components, and access components. I hope the definition is now clear.

### Different types of Context

There are many ways you can get a hold on context (**bad design spotted**).

Most of the time we use one of the following when we need context:

```
- Application instance as context- Activity	- Instance of your activity (this)	- getApplicationContext() in Activity	- getBaseContext() in Activity- Fragment	- getContext() in Fragment- View	- getContext() in View- Broadcast Receiver	- Context received in broadcast receiver- Service	- Instance of your service (this)	- getApplicationContext() in Service- Context	- getApplicationContext() in Context instance
```

I divide context types into two categories: **UI Context** and **Non-UI Context**. This distinction will help you understand `_n-ways_` a little better.

#### UI Context

In reality, only the [ContextThemeWrapper](https://developer.android.com/reference/android/view/ContextThemeWrapper) is UI Context — which means **Context + Your theme**.

Activity extends `ContextThemeWrapper`. This is the reason that, when you inflate any XML, your views are themed. If you inflate your layout with Non-UI context, your layout will not be themed. Go ahead, try it.

When you use Activity as a placeholder for Context, you are guaranteed to be using UI Context. If you use the getContext method from Fragment, you are indirectly using Activity (if you attached Fragment via fragmentManager in activity).

But `view.getContext()` is not guaranteed to be UI Context.

If View was instantiated using Layout Inflater and passed UI Context, you get UI Context back. But if it was instantiated by not passing UI Context, you get the other context back.

```
UI Context- Activity	- Instance of your activity (this)- Fragment	- getContext() in Fragment- View	- getContext() in View (if View was constructed using UI-Context)
```

#### Non-UI Context

Anything except UI Context is Non-UI Context. Technically, anything which is not ContextThemeWrapper is Non-UI Context.

Non-UI Context is allowed do **almost** everything UI-Context can do (**bad design spotted**). But as we pointed out above, you lose theming.

```
Non-UI Context- Application instance as context- Activity	- getApplicationContext() in Activity- Broadcast Receiver	- Context received in broadcast receiver- Service	- Instance of your service (this)	- getApplicationContext() in Service- Context	- getApplicationContext() in Context instance
```

**Tip**: All context types are supposed to be short lived except Application context. This is the one you get from your application class or from using the `getApplicationContext()` method when you have context access.

#### Summary

We have simplified it a little bit by putting Context in two buckets. UI Context is Context + Theming, and technically any class which is a subclass of `ContextThemeWrapper` comes in this bucket. Non-UI Context is all other types of Context.

### Where to use what

The question arises: what will go wrong if you use context in the wrong place? Following are a few scenarios:

#### Scenario 1

Lets say you are inflating a layout and you use Non-UI Context. What may go wrong? You can guess in this case: you will not get a themed layout. Not so bad, hmm? It’s bearable.

#### Scenario 2

You pass UI-Context to someplace where all it needs is resource access or file system access. What can no wrong? Short Answer: Nothing. Remember, UI-Context = Context + Theme. It will gladly serve as context for you.

#### Scenario 3

You pass UI-Context to someplace where all it needs is resource access or file system access **but** it is a long operation in the background. Say downloading a file. Now what can go wrong? Short Answer: Memory leak.

If you are lucky and download completes quickly, the object is released and everything is fine. Sun is shining and birds are chirping. This is one of the most common mistakes developers make. They pass the reference of UI-Context to long living objects, and sometimes it has zero side effect.

However, sometimes Android wants to claim memory for either one of your next component’s requirements or another component’s requirements, and woooshhhh!!! You run out of memory in your app. Don’t worry, I will explain.

#### Memory Leak or Crash! That’s it.

Yes this is the worst case scenario when you use context in the wrong place. If you are new to the app development world, let me share some wisdom. Memory leaks are inversely proportional to your experience. Every Android developer has leaked memory. There is no shame in doing so.

Shame is when you repeat the mistake again and leak it the same way. If you leak memory a different way every time, congrats you are growing. I have explained what a Memory leak is with a short story [here](https://gaurav-khanna.in/blogs/android/mastering-android-context/chapter-3/).

#### Okay I get it, but what is the relation of Context here?

Say it aloud, “Bad Design Spotted".

Almost everything in Android needs access to Context. Naive developers pass UI Context, because that’s what they have access to very easily. They pass short-living context (usually Activity context) to long living objects and before the memory/money is returned back to system, they hit a crisis. Woooshhh!!!

The simplest way to deal with this is with Async Task or Broadcast Receiver. But discussing them isn’t in the scope of this article.

#### Summary

* Do you need to access UI related stuff? Use UI-Context. Inflating Views and showing dialogue are the two use cases I can think of.
* Otherwise, Use Non UI Context.
* Make sure you do not pass short-living context to long-living objects.
* Pass knowledge, help people, plant trees and invite me for a coffee.

### Tips and Tricks

What is the difference between `this`, `getApplicationContext()` and `getBaseContext()`?

This is one question every Android developer have encountered in their lives. I will try to simplify it as much as possible. Let’s take a step back and revisit the basics.

We know there are many factors in mobile devices. For instance, configuration changes all the time, and locale can change explicitly or implicitly.

All of these changes trigger apps to re-create so they can pick the right resources that are the best match to their current configuration. Portrait, Landscape, Tablet, Chinese, German, and so on. Your app needs the best possible resources to deliver the best user experience. It is the Context which is responsible for delivering those best match resources.

Try answering this question:  
The user’s configuration is currently in portrait and you want to access landscape resources. Or the user locale is `en` and you want to access `uk` resources. How will you do it?

Below are some magical methods from Context:

![Image](https://cdn-media-1.freecodecamp.org/images/pm0XjARPJfj3jaVp6O846mROEem3fKcYVOS1)

There are many createX methods, but we are mainly interested in `createConfigurationContext`. Here is how you can use it:

```
Configuration configuration = getResources().getConfiguration();configuration.setLocale(your_custom_locale);context = createConfigurationContext(configuration);
```

You can get a hold of any type of Context you desire. When you call any method on the new Context you just got, you will get access to resources based on the configuration you had set.

I know it is amazing. You can send me thank you card.

Similarly, you can create a Themed Context and use it to inflate views with the theme you want.

```
ContextThemeWrapper ctw = new ContextThemeWrapper(this, R.style.YOUR_THEME);
```

Let’s come back to the tricky question we asked above and discuss Activity Context.

What is the difference between `**this**`**, `getApplicationContext()`** and `**getBaseContext()**`**?**

These are the possible ways you can get a hold on Context when you are in the `Activity` scope.

`this` points to Activity itself, our UI Context and short life context. `getApplicationContext()` points to your application instance which is Non-UI and long living context.

`**baseContext**` is the base of your Activity Context which you can set using a delegate pattern. You already know you can create Context with any `xyz` configuration you want. You can combine your `xyz` configuration knowledge with Base Context and your Activity will load resources as you desire.

Here is the method you can use:

```
@Overideprotected void attachBaseContext (Context base) {super.attachBaseContext(useYourCustomContext);}
```

Once `BaseContext` is attached, your Activity will delegate calls to this object. If you do not attach to Activity, it remains `baseContext` and you get Activity when you call `getBaseContext`.

### Conclusion

We can say Context is the life of your android app. From Android’s point of view, it is your app. You can do almost nothing without Context. Without it, your app is plain Java code.

#### Context + Java code => Android

Good or bad, it is the design we have and we have to make the best of it. From the first part of this article, we learned that we use it to communicate between components, instantiate components, and access components.

In the next part, we learned that Context can be UI or NonUI, Short Lived or Long lived.

Following that, we learned that you need to choose context carefully otherwise you have to deal with memory leaks and other UI issues.

Finally, you saw that Context is responsible for loading best match resources for your app and you can configure it as you want. We also learned the difference between `this`, `applicationContext` and `baseContext`.

Many developers will advise you to use only application context. Do not use Application Context everywhere from the fear of a memory leak. Understand the root cause and always use the right Context in the right place.

You, my dear friend, are a master of Android Context now. You can suggest the next topic you want to understand. [Click here to suggest](https://goo.gl/forms/Du4zTz1MleQsWHHu2).

Below are links from the original Series [**Mastering Android Context**](https://gaurav-khanna.in/blogs/android/mastering-android-context/) on my blog.

#### [Chapter 1](https://gaurav-khanna.in/blogs/android/mastering-android-context/chapter-1/)

What the heck is Context? Why do we need it and what are various use cases in day to day development?

#### [Chapter 2](https://gaurav-khanna.in/blogs/android/mastering-android-context/chapter-2/)

Simplifying Context. We will discuss how many types of context are there and which ones are you suppose to use.

#### [Chapter 3](https://gaurav-khanna.in/blogs/android/mastering-android-context/chapter-3/)

Where to use UI Context and where to use Non UI-Context. How using context at wrong place may lead to memory leaks.

#### [Chapter 4](https://gaurav-khanna.in/blogs/android/mastering-android-context/chapter-4/)

My UI Context also offers me multiple types of context. Let’s answer this question and see how to avoid common pitfalls.

#### [Training](https://gaurav-khanna.in/training/)

Do you know that many times your app is crashing because your developers are not using Context properly? Let’s learn together. [I offer training in Android, Java, and Git.](https://gaurav-khanna.in/training/)

Want to master [Android themes](https://gaurav-khanna.in/blogs/android/mastering-android-themes/)? Check out our series with more than 3k upvotes.

Feel free to share your feedback and questions. Happy Coding.

Follow me on [Medium](https://medium.com/@gaurav.khanna) and [Twitter](https://twitter.com/khanna2402) for updates.

