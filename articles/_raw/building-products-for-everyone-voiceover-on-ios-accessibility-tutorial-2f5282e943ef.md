---
title: How to build apps for everyone using VoiceOver on iOS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-19T17:04:02.000Z'
originalURL: https://freecodecamp.org/news/building-products-for-everyone-voiceover-on-ios-accessibility-tutorial-2f5282e943ef
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ClYE1SfHWy4XYzSDrlK3ug.jpeg
tags:
- name: Accessibility
  slug: accessibility
- name: Design
  slug: design
- name: iOS
  slug: ios
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Jayven N

  Getting started with accessibility


  There’s always those topics that people don’t talk about enough. Sometimes, those
  topics happen to be the most important ones. Accessibility is one of those topics.

  Goal

  This article talks about why acc...'
---

By Jayven N

#### Getting started with accessibility

![Image](https://cdn-media-1.freecodecamp.org/images/Vv7jyJkcf6i4lRZs6UMtuVokbfLXWg-hNoZs)

There’s always those topics that people don’t talk about enough. Sometimes, those topics happen to be the most important ones. Accessibility is one of those topics.

### Goal

This article talks about why accessibility is important and how you can step into the shoes of a VoiceOver user.

### Introduction

People have disabilities.

A lot of people have disabilities.

Disability is normal.

Disability doesn’t have to be something dramatic like breaking a bone. It can be a right shoulder pain that prevents me from doing Exercise A. Hence, I am disabled to do Exercise A. Exercise B, on the other hand, is as effective a shoulder exercise as Exercise A. And, it is for possible for people with and without right shoulder pain.

One in six people in the United States has one or more disabilities.

Yes, one in six. Look around the room. Count one to six. One of you statistically has a disability.

**Disabilities are real and relevant.**

Everyone eventually and naturally deteriorates with time. Brain, muscles, eyes, and ears work differently with time. Everything changes with time. Humans are no different.

Let’s talk about why accessibility is important and how to get started building apps with accessibility in mind.

### Why build an accessible app?

#### Benefit #1: it feels great

Feels great to do great things. You can leave the world a little better than you found it. There’s nothing like sleeping like a baby knowing you have given the world everything today for a more inclusive tomorrow. Making a positive impact according to your ideologies always feels great.

#### Benefit #2: audience size

What if you could increase your revenue by 16.7% by simply supporting accessibility users? That sounds like a very fair deal.

If a company is making 100,000,000 USD per year, they could be making 117,000,000 USD by implementing accessibility features. This is by making the app available to a wider range of users.

Here’s the thing, no one wants to be left out of a great party. If you have a great party, you probably want to invite a lot of great people. If you have a great app, you probably want a lot of people to experience your masterpiece as well.

Say the invitation letters are sent out. The invitation letters reach the mailboxes. The invitees happily open the invitation letters and scream YES! into the sky.

Now let’s talk about getting to your party: everyone has a preferred form of transportation. People may travel by car, motorbike, helicopter, private jet, or jetpack.

Now imagine how tragic your party would be if you left out the jetpackers. So, you decide to register the jetpack air lanes to your house. Consequently, jetpackers can now drop by your party.

How great is that? Your party gets more fun and jetpackers get to enjoy the party as well. Everyone wins.

If your app does not support certain ways of using it, then people may find it difficult to navigate your app. They will decide to not use your app altogether. We can mitigate that and bring the jetpackers onboard.

#### Benefit #3: building an accessible app is hard

Common complaints about developing accessibility features:

* Slow development speed
* Insufficient resources
* The “I have no idea where to begin” thought

These are valid points.

It takes effort to convince the people around you to give you time and space to implement accessibility features in your app.

It takes courage to risk your name and equity to convince the CEO that accessibility features are worthwhile.

Even if you convince everyone to pay attention to accessibility, you may still be left with a page of questions on what to do next. Given the fact that accessibility is so little talked about, your research may not be helpful as you hoped it would be.

And the truth is:

> Yes.

> It is hard.

> But, hard is good.

Here’s the thing. Adding accessibility features to your app is the right thing to do. Beyond being the right thing to do, adding accessibility features can help your app and company take leaps forward and differentiate themselves.

Name five companies off of the top of your head that care about building accessible apps.

I’ll wait…

That’s right. Probably less than five.

If building accessible apps were easy, then everyone would do it because it reaches a larger audience.

But because building accessible apps is hard, you can differentiate yourself. You do something that most people would rather not do. Yet, the impact you can have can be life-changing for some users.

#### Benefit #4: discover your app’s design flaws

Every iOS device has a built-in VoiceOver feature. VoiceOver is iOS’s screen reader. Screen readers empower people with the ability to listen to words on a screen. For people who find it difficult to read with their eyes, they can also absorb information with their ears.

VoiceOver helps you discover app design flaws. Later in the article, you will learn how to use VoiceOver.

To discover app design flaws, you simply need to navigate an app with VoiceOver on. The VoiceOver feature turned on usually means that a user can hardly see what’s on the screen. This means you should be able to navigate without visual dependency.

Then, answer the following questions:

* Does the app sound right?
* Does the app take too much time getting from point A to point B?
* Does the app present UI and layouts in chronological order based on sound alone?

These issues can be explicitly exposed by VoiceOver and can give you new design perspectives. You can use VoiceOver to help improve your app’s navigation, simplicity, and organization.

#### Benefit #5: spread your app with word of mouth

Word of mouth is one of the greatest message-spreading mechanisms. Ever wanted to get the attention of someone? One of the best possible ways to do so is to have an introduction. This is because word of mouth can hold a lot of trust.

Imagine a man named Jon Mack. He happens to have poor eyesight. He’s using Not Accessible App A, Not Accessible App B, and Not Accessible App C. All the apps happen to be poorly designed for people with visual impairment.

Jon is a capable person. Jon has friends. Jon and his friends are moving towards the elderly age.

One evening, Accessible App comes along. The app is designed with a wide audience in mind. Jon uses Accessible App. He loves it.

Jon shares Accessible App with friends, family members, and colleagues.

Jon speaks into the megaphone. Accessible App spreads and does so with word of mouth. Accessible App wins. Jon and his people also win. This is a win-win situation.

When your app is exceptional, people want to share your app. People share your app because it says something about them.

Your users are important, so let’s make them feel important.

Time to take action.

### Where to begin

Let’s understand how one of your VoiceOver users may use your app.

We are going set up VoiceOver on iOS.

#### Setting up VoiceOver on iOS

Unlock your iOS device.

Open the **Settings** app.

Tap **General**.

![Image](https://cdn-media-1.freecodecamp.org/images/UChK9z2ihhlmezfUvgIGvq58A2QDNeo4tKu7)

Tap **Accessibility**.

![Image](https://cdn-media-1.freecodecamp.org/images/16s7CAfLWVpS2FKtTjK4I26KWkBoNJ5WkOXy)

Tap **Accessibility Shortcut**.

![Image](https://cdn-media-1.freecodecamp.org/images/pjJje2y1bBOAgITTNhER4aS8GV76mUlkWbXc)

You should see a list of built-in accessibility features.

Tap on **VoiceOver**.

![Image](https://cdn-media-1.freecodecamp.org/images/n27lI17e86JnlSs9TSLv7yw3Ic1-3kdXkGvQ)

Great.

Now, swipe up from the **Settings** app to enter the home layout.

![Image](https://cdn-media-1.freecodecamp.org/images/LkoSRm8TtlmW-VunZrXz5jipNdUA9SG-o31V)

### Navigating iOS with VoiceOver

Time to give VoiceOver a go. Here are useful four gestures for using VoiceOver:

1. Swipe left or right — navigate the UI

2. Double-tap — select

3. Swipe up or down — choose from available options if any

4. Swipe up from the bottom with a single vibration — exit to home

Let’s put the action hat on. Let’s begin using VoiceOver.

**Triple-click** the power button.

![Image](https://cdn-media-1.freecodecamp.org/images/n2QwR1f1jWA207JQoQ0rbktOwETXb69EgCFC)

VoiceOver is turned on.

Now, swipe right until the **Settings** app is in selection.

Double tap to open the **Settings** app.

![Image](https://cdn-media-1.freecodecamp.org/images/w0jx7AkFhsP1ylY5CtqQGUKmxXeyx3QZr8Mi)

Great.

Now, swipe right until **General** is selected.

Double tap to select **General**.

![Image](https://cdn-media-1.freecodecamp.org/images/b1LxT1-4u4yKf1kcH37jopImpV-gNcNV1j6H)

Swipe right until **Accessibility** is selected.

Double tap to select **Accessibility**.

![Image](https://cdn-media-1.freecodecamp.org/images/lJc8iXIM6rjPnP9PyUtCmfTEc8uGhJMUn3Sa)

Swipe right until **VoiceOver** is selected.

Double tap to select **VoiceOver**.

![Image](https://cdn-media-1.freecodecamp.org/images/CnUEPCNVCjvXZSQNFrNI0xCXp2UPboCM2dgD)

Swipe right until the **Speaking Rate**’s slider is selected.

Swipe up or down with one finger quickly to adjust the speaking rate.

![Image](https://cdn-media-1.freecodecamp.org/images/WUOlj4RvRtCzundoZPWqcu8TqXV147qS0Axs)

Once you have your desired speaking rate, swipe up from the bottom with a single vibration to exit to home.

![Image](https://cdn-media-1.freecodecamp.org/images/ICXsddJBrgdzkMWkhLPZLmsipCtjGY4EFsb7)

So, turns out that VoiceOver is quite practical. You can turn almost anything on iOS into an audiobook.

I’ve definitely found myself using VoiceOver as often as every day to read text on iOS. This reduces the cognitive load. At the same time, it can increase comprehension due to the reading and listening combination.

You are amazing. You’ve just taken the hardest step. The step that fewer people have taken. The first step. Congratulations, you’ve increased your ability to empathize and put yourself in the shoes of many more people. You are on track to build even more exceptional apps.

### CHALLENGE: Use your app blindfolded

Here’s a method to benchmark your app’s accessibility.

Turn on VoiceOver.

Three-finger triple tap.

![Image](https://cdn-media-1.freecodecamp.org/images/yamurZqDKLCOF7oBqWrMS9Yfgv5nuIpDmDYJ)

This turns curtain mode on and your screen becomes pitch black.

Now, navigate your app with VoiceOver with curtain mode on.

When your app’s navigation is effortless with curtain mode, you’re onto an exceptionally accessible app.

### Final remarks

I believe making apps accessible pushes humanity in the right direction. Building an exceptional app experience for all users is a win for the app makers and the users.

I hope to see more of our favorite apps fully support accessibility features.

Please share this article if you have found this article helpful.

### Special thanks

This article is possible thanks to Daud A., Kane C., Esther H., Todd K., Tim C., Tim I., Lilit B., Cliff W., and Shawn.

### Enterprise solutions

For interested enterprises, I recommend you to [reach out to 2359 Media for enterprise solutions](http://2359media.com/contacts/).

