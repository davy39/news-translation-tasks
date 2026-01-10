---
title: Why I Switched to React Native to Create a Super Easy Bottom Sheet
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-04-18T22:30:00.000Z'
originalURL: https://freecodecamp.org/news/i-switched-to-react-native-and-created-a-bottom-sheet-its-easier-than-native
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b91740569d1a4ca2ca4.jpg
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
- name: React Native
  slug: react-native
seo_title: null
seo_desc: "By Ayusch Jain\nI recently switched jobs, and one of my first tasks was\
  \ to create a bottom sheet in React Native. \nComing from a native Android development\
  \ background, I thought it was going to be as daunting as creating a bottom sheet\
  \ in native. But ..."
---

By Ayusch Jain

I recently switched jobs, and one of my first tasks was to create a bottom sheet in React Native. 

Coming from a [native Android development](https://ayusch.com/) background, I thought it was going to be as daunting as creating a bottom sheet in native. But I was so wrong! I was so mesmerized that I decided to write a simple tutorial on creating a bottom sheet in React Native.

A bottom sheet is a useful component that slides up from the bottom of the screen and often contains different options. It's very common in modern design and used by apps such as Uber, Zomato, and many more.

Here's what the final result will look like:

![Image](http://ayusch.com/wp-content/uploads/2020/03/tuxpi.com_.1585128093.jpg)
_Source: https://ayusch.com/_

So let’s take a look at how to create a bottom sheet in React Native.

## Getting Started

First, create a new project in React Native. I’m using expo-cli for this. If you're unaware of expo-cli or just getting started with React Native, check out [this link](https://reactnative.dev/docs/getting-started). 

I’ve named my project BottomSheetDemo.

Next up, we’ll need to install react-native-modalbox. This provides us with many inbuilt capabilities such as animations, positions, backdrops etc.

> $ expo install react-native-modalbox@1.7.1

Note: Remember to install version 1.7.1. The latest version has a bug where backdropPressToClose doesn’t work.

## Creating the Modal

It’s time to create our modal. Remove the code that you’re provided with in the beginning and add the following to your App.js file:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/carbon.png)

This is the bare bones of our bottom sheet/modal. We’ll just show at text at the center of the modal.

## Adding Interaction

We need the bottom sheet to show up when a button is pressed. Let’s add some interaction.

I’ll be adding a simple button in the middle of the screen:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/carbon--1-.png)

On clicking this button, we need to show/hide our bottom sheet. To do this, we’ll maintain a state using the useState React hook.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/carbon--2-.png)

Our modal has a prop named “isOpen” that we can toggle to show/hide our bottom sheet. To show it we’ll simply set modalVisible to false and vice-versa.

But first, let’s separate out our modal from the rest of the code as it is starting to get a bit messy. I’ll create a separate function which will return my modal.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/carbon--3-.png)

The code looks much cleaner now. But our bottom sheet still doesn’t look exactly like a bottom sheet. We need to add some styling.

## Let’s add some Styling!

Create a stylesheet and add the following styles to it:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/carbon--4-.png)

Here’s what the final code looks like:

![Image](https://www.freecodecamp.org/news/content/images/2020/04/carbon--5-.png)

We’ve finally created our bottom sheet in React Native. It is so simple and much easier to create than in native Android. 

I can’t comment on iOS since I’ve never tried that.

So, if you’re an iOS developer or have experience creating a bottom sheet in iOS, let me know what your experience was.

Join the AndroidVille [SLACK](https://rebrand.ly/73lbl3)  workspace for mobile developers where people share their learnings about the latest in tech, especially Android Development, RxJava, Kotlin, Flutter, and mobile development in general.

[Click on this link to join the workspace. It’s absolutely free](https://rebrand.ly/73lbl3).

_Like what you read? Don’t forget to share this post on [Facebook](https://www.facebook.com/AndroidVille), Whatsapp, and_ [_LinkedIn_](https://www.linkedin.com)_._

_You can follow me on [LinkedIn](https://www.linkedin.com/in/ayuschjain), [Quora](https://www.quora.com/profile/Ayusch-Jain), [Twitter](https://twitter.com/ayuschjain), and [Instagram](https://www.instagram.com/androidville/) where I answer questions related to Mobile Development, especially Android and Flutter._

