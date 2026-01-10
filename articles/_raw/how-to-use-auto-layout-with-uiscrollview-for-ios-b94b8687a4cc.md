---
title: How to use Auto Layout with UIScrollView for iOS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-25T16:16:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-auto-layout-with-uiscrollview-for-ios-b94b8687a4cc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*rWN6HdC61ChO2dNs8W8wEQ.jpeg
tags:
- name: Design
  slug: design
- name: ios app development
  slug: ios-app-development
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Sam Ollason

  I love building tools with software, and that is why I am currently the Lead Developer
  for Green 13 Solutions.

  Recently I have been having lots of fun using Swift and the Interface Builder in
  Xcode to create iOS apps.

  I ran into some c...'
---

By Sam Ollason

I love building tools with software, and that is why I am currently the Lead Developer for [Green 13 Solutions](http://irisd.green13solutions.com/).

Recently I have been having lots of fun using Swift and the Interface Builder in Xcode to create iOS apps.

I ran into some challenges when I was trying to create a **scene** where users can **scroll** to see content that overflows in the current **content view**. The content wasn’t scrolling properly and the text wasn’t automatically being shown properly for different screen sizes.

Here are some notes for my future self to refer to. I hope you find them useful as well!

Here is a [repository](https://github.com/SamOllason/autolayout-scrollview-example) for the project if you want to see the completed example.

### What we will build

Our app will have a single page. The page will contain some text and users can scroll down to see the text that overflows from their current content view.

We will use the Interface Builder in Xcode to add a UIScrollView object, a nested UIView object and then a further nested UITextView object. We will use the Interface Builder to add constraints to these elements. The constraints will mean that Auto Layout can enable scrolling to happen properly and the Text View will automatically appear properly on different screen sizes.

### A swift bit of background info (pun intended)

The UIScrollView object can be used as a parent object to other UIKit items such as UIView and UITextView.

Doing this means that all child objects can **collectively have their origin shifted** relative to the **content view** that is shown to the user. This means ‘scrolling’ behaviour works as users expect. Another benefit is that Auto Layout will properly size our elements on different screens as expected.

We use the terms ‘UIScrollView’ and ‘Scroll View’ interchangeably below, and similarly for View and Text View.

Below are the steps to follow.

### Adding View

Create new project and selecting ‘Single View App’. If you click on Main.storyboard and you will see we have a scene with a blank View element.

### Adding Scroll View

Drag a Scroll View UI element from the Object Library into the scene. Then add the constraints shown in the picture below to anchor the Scroll View element to the edges of its parent Safe Area.

![Image](https://cdn-media-1.freecodecamp.org/images/Jhaxfl2emel8kPk8TwfmUSLlJSoPciBhfibi)

### Add a View element

Use the Object Library to drag a View element into the scene. The View will be the parent container for our Text View element.

Manually resize the View element with your cursor so that it fills the width of the screen.

![Image](https://cdn-media-1.freecodecamp.org/images/MKboKx-1Pr9cG-z5Po9jigJc6BK01-TororP)
_Manually resized View element to fit into width_

### Anchor View to Scroll View

Click on the View element in the object hierarchy and drag+release your cursor onto the Scroll View element above it in the hierarchy. Click on the 4 topmost options to apply these constraints. Click on the ‘Equal Widths’ to apply this constraint also.

**Why?** Constraining the View this way means that a child Text View element we add works properly with Auto Layout. This happens because we constrain the Text View to the bottom of the View (which we anchored properly to the bottom of the Scroll View!) instead of directly to the bottom of the Scroll View.

You will see that the layout guides in the Interface Builder are red because there is some other error. We will fix this shortly.

![Image](https://cdn-media-1.freecodecamp.org/images/cGgPMQiJhTMXXpSUXQYKFP9uiKqDNkonUiJw)
_Add these constraints to the View element_

### Add Text View as child to View

Add a Text View element inside the View element in the scene.

### Add constraints to the Text View

Add the constraints in the picture below to the Text View.

**Why?** This will constrain the Text View relative to the View object that is surrounding it.

![Image](https://cdn-media-1.freecodecamp.org/images/NhKkvtmYB37I7gGULPDI-a7idl2KWN7mlcex)
_Adding constraints to Text View_

### Disable scroll behaviour in Text View

You should have a similar screen to the one below. You can see that there is still a lot of red in the Interface Builder.

You can remove these warnings by selecting the Text View element and **deselecting the ‘Scrolling Enabled’ in the editor pane** on the right hand side.

![Image](https://cdn-media-1.freecodecamp.org/images/C2yKd3qiiQtqIVmO4A5FV7oCpMuB9KyFaevK)
_Deselect ‘Scrolling Enabled’ on the right to remove these red errors_

Note that we will still have scroll behaviour with this approach but **it will be the parent Scroll View that is actually being moved, not the individual Text View element**. Its the same as how a leaf only moves on a river because the river that surrounds it is moving!

This is slightly subtle but quite important to understand as it underpins the whole solution.

![Image](https://cdn-media-1.freecodecamp.org/images/JjCnsnOxlF0Cp5akdGf9wDrOvWUexcPe9jXd)
_Our approach means a Text View only scrolls because a Scroll View moves it — same as how a leaf only moves because the surrounding river moves it_

### Finally

Add some more content to the Text View. You should see that scrolling works as expected and that the Text View appears properly on different screen sizes.

This is the beauty of Auto Layout!

![Image](https://cdn-media-1.freecodecamp.org/images/YuajWxyO9HnRMGpONlOhgGA7iXZ5wOajtCqL)
_Screenshot of scrolled Text View using Xcode Simulator_

Here is a [repository](https://github.com/SamOllason/autolayout-scrollview-example) for the project if you want to see the completed example.

All information about robins for the Text View content is directly from [Wikipedia](https://en.wikipedia.org/wiki/European_robin). Thanks to the community for this.

_Why robins?_ Because I love birds and robins are particularly awesome creatures!

Thanks for reading, I hope you found this useful. Please let me know if you have any comments of questions!

