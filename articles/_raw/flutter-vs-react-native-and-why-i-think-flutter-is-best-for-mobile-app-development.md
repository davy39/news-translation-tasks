---
title: Flutter VS React Native – And Why I think Flutter is Best for Mobile App Development
subtitle: ''
author: Tomer
co_authors: []
series: null
date: '2019-01-18T22:26:00.000Z'
originalURL: https://freecodecamp.org/news/flutter-vs-react-native-and-why-i-think-flutter-is-best-for-mobile-app-development
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca64b740569d1a4ca6f40.jpg
tags:
- name: Flutter
  slug: flutter
- name: mobile app development
  slug: mobile-app-development
- name: React Native
  slug: react-native
seo_title: null
seo_desc: "This isn’t the type of article you might think it’s going to be. I’m not\
  \ going to list the pros and cons of every framework and I am not going to do a\
  \ comparative analysis of performance. \nOver the past few weeks, I have dipped\
  \ my coding hand in tryi..."
---

This isn’t the type of article you might think it’s going to be. I’m not going to list the pros and cons of every framework and I am not going to do a comparative analysis of performance. 

Over the past few weeks, I have dipped my coding hand in trying to create simple, functional applications using both frameworks. The title of this article is the conclusion I have come to from my experimentation.

_⚠️ Disclaimer: I am in no way stating that framework A is better than framework B and I have not been paid by neither to give my opinion. This is solely an article based on my personal experience and nothing more._

## Some Background

While I am not familiar with either [Dart](https://www.dartlang.org/) or [React](https://reactjs.org/), I have some background in JavaScript and more than my fair share of Native development. Since these two frameworks are relatively new and are offering the same type of development experience, I thought I’d give them a try to see what the whole fuss is about. Granted, I am not profoundly adept in the whole logic of both and I have yet to fully understand the state component in React or the component hierarchy in Dart. With that being said, I set out to create a basic application in both platforms. The premise for the application? One that would accept user input, and on a touch of a button will display the user input in some sort of list that the user can scroll through on the screen.

---

# My REACT-ion

I first started working on the application using **_React Native_**. Setting up the project was _very_ simple. All you had to do was follow through on the instructions in the [Getting Started documentation](https://facebook.github.io/react-native/docs/getting-started.html). I installed **_Expo_** and within minutes, my application was loading on my phone. I really appreciated the speed in which the QR code scanner of the Expo application identifies the code on the screen. Expo’s interface on the computer was also really straight forward. You can see the status of the application (building or failing), boot up an Android/iOS emulator and more. Now it was time to put my own logic into the application. This is where things got frustrating.

Swapping the View element with a text input was easy, and so was adding a button with an onClick action. But trying to have a data set to save the user input, was down right mind boggling. I made a variable which was an array in the state object and tried various ways to update it when the user finished entering his/her own input. I have searched high and low and implemented various solutions to allow my application to save data to the array, but to no avail. The documentation I did find was sparse and it wasn’t really helpful. Not to mention the plethora of compilation errors I was having, which were not that instructive into what was wrong with my code. After a while, it became quite annoying seeing that red screen repeatedly.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/1_QwBpjtvPlj0B8YZ6Mc1VIA.png)
_Why React? Why?_

# Fluttering Away

Being flustered and ashamed I couldn’t make the simplest of applications using React, and following the announcement of Flutter, I thought I’d take a crack building the same application. **_You know what they say, change of place - change of luck._**

Setup was a breeze and offered the same quick experience React afforded and I was ready to start developing in no time. Downloading the Flutter SDK and installing the plugin were part of just a few simple steps to start developing in Flutter.

Next came the task of looking at the code. How can I put it into words? Not what I was expecting. You have different components in a long and winding hierarchy, which at times, can be difficult to keep track of. Apart from that, you have widgets and columns and rows and you need to figure out where everything fits in together. By now, you are thinking I am supposed to tell you why I like Flutter. As most things are, they have their strengths and weaknesses. And after going over the things I think are irritating, I can relish in what I found endearing.

For starters, Flutter is heavily [documented](https://flutter.io/docs). Every time I had to look up for something, I could easily find it in the documentation. More so, there are so many real life examples of various applications out there, that you are bound to find one similar to something that you are trying to make.

After tinkering with the starter code, you start to get a hang of the hierarchy, and how views are displayed, that you come to understand the weird intricacies of it all. It was also a blast to realize that making a component behave a certain way was as easy as adding another characteristic to the widget.

And above all, **_I was already in a native setting_**. I was at home with Android Studio, understanding where everything goes and enjoying the luxuries and benefits of a familiar surrounding.

Compared to the time I spent **_trying_** to develop my application in React, the time I spent in Flutter was a fraction of that. Plus, even if what you are trying to do doesn’t always work, you get the sense of eventual progress and you are encouraged to look at things in more detail inside the documentation.

Angry ?? Upset ?? Exhilarated ?? Jubilant? ? Let me know what you think.

