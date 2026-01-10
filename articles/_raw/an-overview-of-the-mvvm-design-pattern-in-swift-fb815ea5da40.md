---
title: An overview of the MVVM design pattern in Swift
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-12T17:07:16.000Z'
originalURL: https://freecodecamp.org/news/an-overview-of-the-mvvm-design-pattern-in-swift-fb815ea5da40
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eSFq7WQEopQBOjggm3MEwA.png
tags:
- name: Design
  slug: design
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Azhar

  This article assumes you are comfortable with the MVC pattern, which is the baseline
  design pattern adopted and recommended by Apple.


  What is MVVM?

  MVVM is a structural design pattern. Imagine that you have two views with a different
  layout...'
---

By Azhar

This article assumes you are comfortable with the MVC pattern, which is the baseline design pattern adopted and recommended by Apple.

![Image](https://cdn-media-1.freecodecamp.org/images/1*eSFq7WQEopQBOjggm3MEwA.png)

### What is MVVM?

MVVM is a structural design pattern. Imagine that you have two views with a different layout that need to be populated with data from the same model class. MVVM allows you to use data from a single model class and represent it in different ways to populate a view.

#### Models

These hold the app data. These are the structs and classes that you have created to hold the data you receive from a REST API or from some other data source.

#### Views

These display UI elements on the screen. These are usually classes that subclass UIView and use UIKit.

#### View Models

These classes are where you take the information from the model classes and transform them into values that can be displayed in a particular view.

### How do I use this?

Use this pattern to transform data from a model class to a representation that works for a different view. For example, you can use a view model to transform a String to an NSAttributedString or a Date into a formatted String.

This pattern is similar to MVC, which is perhaps why it is relatively simple to add it to an MVC codebase. All you need to do is simply add your view model classes to the existing codebase and use them to represent the data as you need it. This does minimize the role of the View Controller, which helps lift some weight off your View Controller classes. You too can avoid ‘Massive View Controller’.

**_Disclaimer_**: MVVM can’t help you avoid a massive view controller problem on its own. You can diversify the load on a view controller class by using design patterns in conjunction with each other, like the delegate pattern, singleton pattern etc.

Let’s see how MVVM works in code.

Open up Xcode and create a new Playground project. Select Single View under the iOS tab to start. Click on the assistant editor (icon with two intersecting circles) to display the Live View window. You should see this.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rZ_OI7oHbdFRT8YLfwItTQ.png)

You can go ahead and delete the MyController class. We will be setting up our views manually.

Let’s pretend we are working on a bird store app. Let’s start by creating a model class for Birds. Right below the closing brace for MyViewController class add the following class.

Every bird has a name, rarity level, and an image. Let’s assume we need to show these properties on a view. The rarity property is an enum that we can’t display on a view without some kind of representation that is useful for a view element to render. This is a perfect time for us to create a bird view model for this representation. Let’s try to display the price of each bird as a string based on the rarity level of the bird.

Add the following class to your playground.

Here’s what’s going on in the view model code:

1. We create a private bird property of type Bird so we can access the properties of the model class. We also write an init method to set the bird property.
2. We create two computed property that get their values from the properties associated with the private bird property. We don’t modify the properties because they are already in the right representation for our view.
3. We create a purchaseFeeText property that is a computed property. This property uses the rarity values from the private bird property to assign a cost using a switch statement. **This is where our view model class is taking data from the model class object and converting it into a representation that we want to use in a view.**

Now let’s write code for the UIView that we will use to display information from the view model class. Add the following class to your playground file.

You can download the image being used by the imageView [here](https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&ved=2ahUKEwiMnIqolaThAhUTbisKHXYhD78QjRx6BAgBEAU&url=https%3A%2F%2Fwww.iconfinder.com%2Ficons%2F1829980%2Fbrand_logo_network_social_swift_icon&psig=AOvVaw25fA-XJq_9BsiEnSwWxchz&ust=1553839488282677). Add it to the Resources folder in the Project Navigator and rename it “swifty.png”.

Now that we have our bird view class set up lets add the code to see it in the playground live view. Add the following after the closing brace of the BirdView class.

Here’s what’s going on

1. We create a new bird instance from the model class named “swifty”
2. We create a new instance from the view model class from the swifty object.
3. We create a frame property and then initialize the BirdView using that frame.
4. We configure the views using the view model instance’s properties.
5. We set the view to the playground live view which then renders everything into the assistant editor.

You can see the live view by selecting **View**&**gt;Assist**a**nt Edi**t**or&g**t**;Show Ass**i**stant** Editor from the top menu bar.

### When do I use this?

If you find yourself needing to use data from a model class in views with different representations of the data it would make sense to use the MVVM pattern. MVVM is probably not going to be the starting point of your app. You will probably start with MVC. Keep an eye on your requirements, you can always introduce MVVM (and most other design patterns) at a later time in your codebase.

