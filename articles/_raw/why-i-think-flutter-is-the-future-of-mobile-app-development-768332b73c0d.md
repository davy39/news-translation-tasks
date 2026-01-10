---
title: Why I think Flutter is the future of mobile app development
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-05-20T17:37:07.000Z'
originalURL: https://freecodecamp.org/news/why-i-think-flutter-is-the-future-of-mobile-app-development-768332b73c0d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YS1KCJ51iHT9vaQAoNOtIA.png
tags:
- name: Dart
  slug: dart
- name: Flutter
  slug: flutter
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Eric Grandt

  I dabbled a bit in Android and iOS development quite a few years back using Java
  and Objective-C. After spending about a month working with both of them, I decided
  to move on. I just couldn’t get into it.

  But recently, I learned about ...'
---

By Eric Grandt

I dabbled a bit in Android and iOS development quite a few years back using Java and Objective-C. After spending about a month working with both of them, I decided to move on. I just couldn’t get into it.

But recently, I learned about Flutter and decided to give mobile app development another shot. I instantly fell in love with it as it made developing multi-platform apps a ton of fun. Since learning about it, I’ve created an app and a library using it. Flutter seems to be a very promising step forward and I’d like to explain a few different reasons why I believe this.

### Powered by Dart

Flutter uses the Google-developed Dart language. If you’ve used Java before, you’ll be fairly familiar with the syntax of Dart as they are quite similar. Besides the syntax, Dart is a fairly different language.

I’m not going to be talking about Dart in depth as it’s a bit out of scope, but I’d like to discuss one of the most helpful features in my opinion. This feature being support for asynchronous operations. Not only does Dart support it, but it makes it exceptionally easy.

This is something you’ll most likely be using throughout all of your Flutter applications if you’re doing IO or other time-consuming operations such as querying a database. Without asynchronous operations, any time-consuming operations will cause the program to freeze up until they complete. To prevent this, Dart provides us with the `async` and `await` keywords which allow our program to continue execution while waiting for these longer operations to complete.

Let's take a look at a couple of examples: one without asynchronous operations and one with.

<script src="https://gist.github.com/Erigitic/ff9f18541183586bc090696f756c2ad0.js"></script>

And the output:

<script src="https://gist.github.com/Erigitic/da16af9aa172410efcb6690218929607.js"></script>

This isn’t ideal. No one wants to use an app that freezes up when it executes long operations. So let’s modify this a bit and make use of the `async` and `await` keywords.

<script src="https://gist.github.com/Erigitic/f30ae96a17de307b8dc0dcb022ba62ed.js"></script>

And the output once again:

<script src="https://gist.github.com/Erigitic/342215b537fabb982cb2f68366b86cd5.js"></script>

Thanks to asynchronous operations, we’re able to execute code that takes a while to complete without blocking the execution of the rest of our code.

### Write Once, Run on Android and iOS

Developing mobile apps can take a lot of time considering you need to use a different codebase for Android and iOS. That is unless you use an SDK like Flutter, where you have a single codebase that allows you to build your app for both operating systems. Not only that, but you can run them completely natively. This means things such as scrolling and navigation, to name a few, act just like they should for the OS being used.

To keep with the theme of simplicity, as long as you have a device or simulator running, Flutter makes building and running your app for testing as simple as clicking a button.

### UI Development

UI development is one of those things that I almost never look forward to. I’m more of a backend developer, so when it comes to working on something that is heavily dependent on it, I want something simple. This is where Flutter shines in my eyes.

UI is created by combining different widgets together and modifying them to fit the look of your app. You have near full control over how these widgets display, so you’ll always end up with exactly what you’re looking for. For laying out the UI, you have widgets such as `Row`, `Column`, and `Container`. For content, you have widgets like `Text` and `RaisedButton`. This is only a few of the widgets Flutter offers, there are a lot more. Using these widgets, we can build a very simple UI:

<script src="https://gist.github.com/Erigitic/38db5a711b2eac9e0b62bef1561e3386.js"></script>

![Image](https://cdn-media-1.freecodecamp.org/images/9hlvITfh5FnClzD6qa-xCsnSz-Zngd38EFV8)

Flutter has more tricks up its sleeve that makes theming your app a breeze. You could go through and manually change the fonts, colors, and looks for everything one by one, but that takes way too long. Instead, Flutter provides us with something called `ThemeData` that allows us to set values for colors, fonts, input fields, and much more. This feature is great for keeping the look of your app consistent.

<script src="https://gist.github.com/Erigitic/a08862fc269e3a3062eada0764301200.js"></script>

With this `ThemeData`, we set the apps colors, font family, and some text styles. Everything besides the text styles will automatically be applied app-wide. Text styles have to be set manually for each text widget, but it's still simple:

<script src="https://gist.github.com/Erigitic/d5e5a4237de9b7c25834efee064ff8c1.js"></script>

![Image](https://cdn-media-1.freecodecamp.org/images/55hxft9gL1AxB7U4xIWcebrMTOpS-TY1Y1Xn)
_Flutter app using the above ThemeData_

To make things even more efficient, Flutter can hot reload apps so you don’t need to restart it every time you make a change to the UI. You can now make a change, save it, then see the change within a second or so.

### Libraries

Flutter provides a lot of great features out of the box, but there are times when you need a bit more than it offers. This is no problem at all considering the extensive number of [libraries available for Dart and Flutter](https://pub.dev/). Interested in putting ads in your app? There’s a library for that. Want new widgets? There are libraries for that.

If you’re more of a do-it-yourselfer, make your own library and share it with the rest of the community in no time at all. Adding libraries to your project is simple and can be done by adding a single line to your `pubspec.yaml` file. For example, if you wanted to add the `sqflite` library:

<script src="https://gist.github.com/Erigitic/e708ca4f736df2c09a5a72bb5940fb20.js"></script>

After adding it to the file, run `flutter packages get` and you're good to go. Libraries make developing Flutter apps a breeze and save a lot of time during development.

### Backend Development

Most apps nowadays depend on some sort of data, and that data needs to be stored somewhere so it can be displayed and worked with later on. So keeping this in mind when looking to create apps with a new SDK, such as Flutter, is important.

Once again, Flutter apps are made using Dart, and Dart is great when it comes to backend development. I’ve talked a lot about simplicity in this article, and backend development with Dart and Flutter is no exception to this. It’s incredibly simple to create data-driven apps, for beginners and experts alike, but this simplicity by no means equates to a lack of quality.

To tie this in with the previous section, libraries are available so you can work with the database of your choosing. Using the `sqflite` library, we can be up and running with an SQLite database fairly quickly. And thanks to singletons, we can access the database and query it from practically anywhere without needing to recreate an object every single time.

<script src="https://gist.github.com/Erigitic/0553aa7f34798154b4c3401a9892150f.js"></script>

After retrieving data from a database, you can convert that to an object using a model. Or if you want to store an object in the database, you can convert it to JSON using the same model.

<script src="https://gist.github.com/Erigitic/fdb293140f3e05ee91793f4595979c23.js"></script>

This data isn’t all that useful without a way to display it to the user. This is where Flutter comes in with widgets such as the `FutureBuilder` or `StreamBuilder`. If you're interested in a more in-depth look at creating data-driven apps using Flutter, SQLite, and other technologies, I encourage you to check out the article I wrote on that:

**[Using Streams, BLoCs, and SQLite in Flutter](https://www.freecodecamp.org/news/using-streams-blocs-and-sqlite-in-flutter-2e59e1f7cdce/)**  
[_Streams, BLoCs, and SQLite make for a great combination when it comes to working with data in your Flutter…_](https://medium.com/@erigitic/using-streams-blocs-and-sqlite-in-flutter-2e59e1f7cdce)

### Final Thoughts

With Flutter, the possibilities are practically endless, so even super extensive apps can be created with ease. If you develop mobile apps and have yet to give Flutter a try, I highly recommend you do as I’m sure you’ll fall in love with it as well. After using Flutter for quite a few months, I think it’s safe to say that it’s the future of mobile development. If not, it’s definitely a step in the right direction.

