---
title: How to create a consistent custom font in an iOS app with just several lines
  of code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-11T22:00:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-consistent-custom-font-in-an-ios-app-e07b1ddb7a7c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VaQCLYc6J3qmNdEPHmhIOA.png
tags:
- name: fonts
  slug: fonts
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: null
seo_desc: 'By Yuichi Fujiki

  In this article, you''ll learn how to create a unified custom look throughout your
  app with these simple tricks.

  What we want to do

  In iOS, there is a mechanism called UIAppearance to define an app’s global configuration.
  For example,...'
---

By Yuichi Fujiki

In this article, you'll learn how to create a unified custom look throughout your app with these simple tricks.

## What we want to do

In iOS, there is a mechanism called `UIAppearance` to define an app’s global configuration. For example, you can set a consistent background color of the navigation bar with just one line :

```
UINavigationBar.appearance().barTntColor = UIColor.blue
```

However, if you apply the same approach to the font like this:

```
UILabel.appearance().font = UIFont(named: "Gills Sans", size: 14)
```

all the `UILabel` instances will indeed have “Gills Sans”, **but with 14pt size as well**. I don’t think any app would want to have **only** 14pt fonts throughout the app. Since `UIFont` always needs the size information to be initialized, there is **no standard way** in `UIKit` to just change the typeface without affecting the size.

But, don’t you want to change the font typeface without hunting down all the Swift files and Interface Builder files? Imagine you have an app with tens of screens and the product owner decides to change the font for the entire app. Or your app wants to cover another language, and you want to use another font for the language because it would look better.

This short article explains how you can do that with just several lines of code.

## UIView Extension

When you create `UIView` extension and declare a property with `@objc` modifier, you can set that property through `UIAppearance`.

For example, if you declare a `UILabel` extension property `substituteFontName` like this:

You can call it in `AppDelegate.application(:didFinishLaunching...)`

```
UILabel.appearance().substituteFontName = "Gills Sans"
```

And voilà, all `UILabel` will be in the “Gills Sans” font with appropriate sizes. ?

## But you want to use bold font as well, don’t you?

Life is good so far, but what if you want to specify two different variations of the same font, like bold font? You would think you can just add another extension property `substituteBoldFontName` and call it like this, right?

```
UILabel.appearance().substituteFontName = fontNameUILabel.appearance().substituteBoldFontName = boldFontName
```

Not that easy. If you do this, then **all** the `UILabel` instances show up in bold font. I will explain why.

It seems that `UIAppearance` is just calling all the setter methods of the registered properties in the order they were registered.

So if we implemented the `UILabel` extension like this:

then setting the two properties through `UIAppearance` results in the code sequence similar to the following at every `UILabel` initialization under the hood.

```
font = UIFont(name: substituteFontName, size: font.pointSize)font = UIFont(name: substituteBoldFontName, size: font.pointSize)
```

So, the first line is overwritten by the second line and you are going to have bold fonts everywhere. ?

### What can you do about it?

In order to solve this issue, we can assign proper font style based on the original font style ourselves.

We can change our `UILabel` extension as follows:

Now, the code sequence that is called at `UILabel` initialization will be as follows, and only one of the two `font` assignment will be called in a condition.

```
if font.fontName.range(of: "Medium") == nil {   font = UIFont(name: newValue, size: font.pointSize)}if font.fontName.range(of: "Medium") != nil {   font = UIFont(name: newValue, size: font.pointSize)}
```

As a result, you will have an app with beautifully unified text style while regular and bold fonts co-exist, yay! ?

You should be able to use the same logic to add more styles like italic fonts as well. Also, you should be able to apply the same approach to another control like `UITextField`.

Hope this helps fellow iOS devs, happy coding!!

