---
title: How to make height collection views dynamic in your iOS apps
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-26T17:45:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-height-collection-views-dynamic-in-your-ios-apps-7d6ca94d2212
coverImage: https://cdn-media-1.freecodecamp.org/images/1*58RjgkbswK_v3ofUG4z_qA.jpeg
tags:
- name: data
  slug: data
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Payal Gupta

  Be dynamic, just like life…


  Table views and collection views have always been an integral part of iOS app development.
  We all might have came across various issues related to them. In this article, we’ll
  discuss one such problem state...'
---

By Payal Gupta

#### Be dynamic, just like life…

![Image](https://cdn-media-1.freecodecamp.org/images/1*58RjgkbswK_v3ofUG4z_qA.jpeg)

Table views and collection views have always been an integral part of iOS app development. We all might have came across various issues related to them. In this article, we’ll discuss one such problem statement related to collection views.

### Problem Statement

Let’s assume we’ve a `UICollectionView` in a `UITableViewCell` and around 20 `UICollectionViewCells` that we need to render in it vertically. We can definitely implement that in the blink of an eye with the given data source.

Now comes the actual problem statement — we need the `UITableViewCell` to adjust its height dynamically according to its content. Also, the `UICollectionView` must be such that all the cells are displayed in one go, i.e. no scrolling allowed.

Long story short: _make everything dynamic…_

![Image](https://cdn-media-1.freecodecamp.org/images/1*QxfoBsPpGFM707gho3k0eA.gif)
_**Fixed and Dynamic Height Collection View**_

### Let’s start coding

A view in iOS calculates its height from its content, given there is no height constraint provided. Same goes for `UITableViewCell`.

For now, we’ll keep a single `collectionView` inside our `tableViewCell` with its `leading, top, trailing and bottom constraints` set to 0.

![Image](https://cdn-media-1.freecodecamp.org/images/1*KOtsApDTjYA4J2oo-1mRYA.png)
_**View Hierarchy**_

Since we haven’t provided any height constraint to the `collectionView` and neither do we know the its `contentSize` beforehand, then how will the `tableViewCell` calculate its height?

#### **Solution**

Dynamically calculating the `collectionView’s` height as per its `contentSize` is simply a 3 step process.

**1.** Subclass `UICollectionView` and override its `layoutSubviews()` and `intrinsicContentSize` , i.e.

The above code will invalidate the `intrinsicContentSize` and will use the actual `contentSize` of `collectionView`. The above code takes into consideration the `custom layout` as well.

**2.** Now, set `DynamicHeightCollectionView` as the `collectionView’s` class in `storyboard`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*w3eFLkfu3BvAg04hj__pPQ.png)

**3.** One last thing, for the changes to take effect: you need to call `layoutIfNeeded()` on `collectionView`, after reloading `collectionView’s` data, i.e.

```
func configure(with arr: [String]) {   self.arr = arr   self.collectionView.reloadData()   self.collectionView.layoutIfNeeded() //Here..!!!}
```

And there you have it!

### Sample Project

You can download the sample project from [here](https://github.com/pgpt10/DynamicHeightCollectionView).

### Further reading

Don’t forget to read my other articles:

1. [Everything about Codable in Swift 4](https://hackernoon.com/everything-about-codable-in-swift-4-97d0e18a2999)
2. [Everything you’ve always wanted to know about notifications in iOS](https://medium.freecodecamp.org/ios-10-notifications-inshorts-all-in-one-ad727e03983a)
3. [Deep copy vs. shallow copy — and how you can use them in Swift](https://medium.freecodecamp.org/deep-copy-vs-shallow-copy-and-how-you-can-use-them-in-swift-c623833f5ad3)
4. [Coding for iOS 11: How to drag & drop into collections & tables](https://hackernoon.com/drag-it-drop-it-in-collection-table-ios-11-6bd28795b313)
5. [All you need to know about Today Extensions (Widget) in iOS 10](https://hackernoon.com/app-extensions-and-today-extensions-widget-in-ios-10-e2d9fd9957a8)
6. [UICollectionViewCell selection made easy..!!](https://hackernoon.com/uicollectionviewcell-selection-made-easy-41dae148379d)

Feel free to leave comments in case you have any questions.

