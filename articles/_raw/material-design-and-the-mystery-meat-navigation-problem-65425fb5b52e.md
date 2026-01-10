---
title: Material Design and the Mystery Meat Navigation Problem
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-27T04:20:09.000Z'
originalURL: https://freecodecamp.org/news/material-design-and-the-mystery-meat-navigation-problem-65425fb5b52e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zWh3_7qHGS1sWYzzEnhaXw.png
tags:
- name: Design
  slug: design
- name: Material Design
  slug: material-design
- name: mobile
  slug: mobile
- name: UX
  slug: ux
- name: ux design
  slug: ux-design
seo_title: null
seo_desc: 'By Teo Yu Siang

  In March 2016, Google updated Material Design to add bottom navigation bars to its
  UI library. This new bar is positioned at the bottom of an app, and contains 3 to
  5 icons that allow users to navigate between top-level views in an ap...'
---

By Teo Yu Siang

In March 2016, Google [updated](http://www.androidauthority.com/bottom-navigation-material-design-guidelines-680207/) Material Design to add bottom navigation bars to its UI library. This new bar is positioned at the bottom of an app, and contains 3 to 5 icons that allow users to navigate between top-level views in an app.

Sound familiar? That’s because bottom navigation bars have been a part of [iOS’s UI library](https://developer.apple.com/ios/human-interface-guidelines/ui-bars/tab-bars/) for years (they’re called tab bars in iOS).

![Image](https://cdn-media-1.freecodecamp.org/images/7YItl6X12sekqS7gEvWob4GYqKgaeBZQHij9)
_Left: Material Design’s bottom navigation bar | Right: iOS’s tab bar_

Bottom navigation bars are [a better alternative](http://www.lukew.com/ff/entry.asp?1945) to the hamburger menu, so their addition into Material Design should be good news. But Google’s version of bottom navigation bars has a serious problem: **mystery meat navigation**.

Whether you’re an Android user, designer, or developer, this should trouble you.

### What’s mystery meat navigation, and why’s it so bad?

Mystery meat navigation is a term coined in 1998 by Vincent Flanders of the famous website [Web Pages That Suck](http://www.webpagesthatsuck.com/). It refers to buttons or links that don’t explain to you what they do. Instead, you have to click on them to find out.

(The term “mystery meat” originates from the meat served in American public school cafeterias that were so processed that the type of animal they came from is no longer discernible.)

![Image](https://cdn-media-1.freecodecamp.org/images/DCG0RcBAYpPo1PiWKyXvJ6udqLMKsAL4orlG)
_An example of mystery meat navigation | [Source](http://gigi.nullneuron.net/gigilabs/on-mystery-meat-navigation-and-unusability/" rel="noopener" target="_blank" title=")_

**Mystery meat navigation is the hallmark of designs that prioritize form over function.** It’s bad UX design, because it emphasizes aesthetics at the cost of user experience. It adds cognitive load to navigational tasks, since users have to guess what the button does. And if your users need to guess, you’re doing it wrong.

You wouldn’t want to eat mystery meat—similarly, users wouldn’t want to click on mystery buttons.

### Strike 1: Android Lollipop’s Navigation Bar

Material Design’s first major mystery meat navigation problem happened in 2014 with Android Lollipop.

Android Lollipop was introduced in the same conference that debuted Material Design, and sports a redesigned UI to match Google’s new design language.

![Image](https://cdn-media-1.freecodecamp.org/images/Wdwchat-pQDuQX5nPu8I8w8ClC9iKK2wEA4T)
_Navigation bar in earlier versions of Android_

One of the UI elements that got redesigned was the navigation bar, the persistent bar at the bottom of Android OS that provides navigation control for phones without hardware buttons for Back, Home and Menu.

In Android Lollipop, the navigation bar was redesigned to this:

![Image](https://cdn-media-1.freecodecamp.org/images/7nRsekkx7N76oZ0R2901z7FLPs0JUBefoSJs)
_Navigation bar, Android Lollipop and up_

See the problem?

While the previous design is less aesthetically appealing, it’s more or less straightforward. The Back and Home icons can be understood without the need for text labels. The 3rd icon is a bit of a mystery meat, but on the whole, the UX of the old navigation bar wasn’t too bad.

The new bar, on the other hand, is _extremely_ pretty. The equilateral triangle, circle, and square are symbols of geometric perfection. But it’s also _extremely_ user-unfriendly. It’s abstract—and navigation controls should never be abstract. It’s full-blown mystery meat navigation.

The triangle icon might resemble a “Back” arrow, but what does a circle and a square mean in relation to navigation control?

![Image](https://cdn-media-1.freecodecamp.org/images/nvOaaRnehcqssATkE4qJY7MzIiba7GoPVrlE)
_Making sense of the navigation bar icons_

### Strike 2: Floating Action Buttons

Floating action buttons are special buttons that appear above other UI elements in an app. Ideally, they’re used to promote the primary action of the app.

![Image](https://cdn-media-1.freecodecamp.org/images/MwpSqGbO5h9GLia5FMdnpsMVsxz0-SbU5BbM)
_Specs for the floating action button | [Source](https://material.io/guidelines/components/buttons-floating-action-button.html#buttons-floating-action-button-floating-action-button" rel="noopener" target="_blank" title=")_

Floating action buttons also suffer from the mystery meat navigation problem. By design, the floating action button is a circle containing an icon. It’s a pure-icon button, with no room for text labels.

The truth is that [**icons are incredibly hard to understand**](http://uxmyths.com/post/715009009/myth-icons-enhance-usability) because they’re so open to interpretation. Our culture and past experiences inform how we interpret icons. Unfortunately, designers (especially, it seems, Material designers) have a hard time facing this truth.

Need proof that icon-only buttons are a bad idea? Let’s play a guessing game.

Below is a list of what—according to Material Design’s [guidelines](https://material.io/guidelines/components/buttons-floating-action-button.html)—are acceptable icons for floating action buttons. Can you guess what each button does?

![Image](https://cdn-media-1.freecodecamp.org/images/YvRDCuTrv7S8S76-ENqYBgS8GI8OjaIwXY-v)
_Mystery button 1_

Ok, that’s a simple one to warm you up. It represents “Directions”.

![Image](https://cdn-media-1.freecodecamp.org/images/2lqEudSZmyNmqGtpjrn4I2RtPYIZDbUnwwYL)
_Mystery button 2_

What about this? If you’re an iOS or Mac user, you might say “Safari.” It actually represents “Explore.”

![Image](https://cdn-media-1.freecodecamp.org/images/UUHgLVPW5MWGIx-1tiy2JAghliERwnjw6gDe)
_Mystery button 3_

Things are getting fun (or frustrating) now! Could this be “Open in contacts”? “Help, there’s someone following me”? Perhaps this is a button for your “Phone a friend” lifeline.

![Image](https://cdn-media-1.freecodecamp.org/images/QqiP6oceM0SVfMXfLxNPs4lajjSleb9kdb2g)
_Mystery button 4_

Hang on, _this_ is the button for “Open in contacts.” Right? Or is this “Gossip about a friend” since the person is inside a speech bubble?

Ready for the final round? Here’s the worst (and most used) icon:

![Image](https://cdn-media-1.freecodecamp.org/images/eYdflx0Iu5vUqPOt2QKCO0LR52ndHAPD9pCt)
_Mystery button 5_

You might think the “+” button is rather simple to understand—it’s obviously a button for the “Add” action. But add _what_?

_Add what:_ that’s the problem right there. If a user needs to ask that question, your button is officially mystery meat. Sadly, developers and designers of Material Design apps seem to be in love with the “+” floating action button.

Precisely because the “+” button _seems_ so easy to understand, it ends up being the most abused icon for floating action buttons. Consider how Google’s own Inbox app displays _additional_ buttons when you tap the “+” floating button, which is not what a user would expect:

![Image](https://cdn-media-1.freecodecamp.org/images/f1EkSce5KKMIhKgbVxSkSisB5GnLbW6uly0y)

![Image](https://cdn-media-1.freecodecamp.org/images/CIE3zt1sLgpfCwGBs0ivSgBkQ8PJYtQ1l9ox)
_The “+” button opens up a menu of… more buttons?_

What makes things worse is how the same icons have different meanings in different apps. Google used the pencil icon to represent “Compose” in Inbox and Gmail, but used it to represent “Edit” in its photo app Snapseed.

![Image](https://cdn-media-1.freecodecamp.org/images/31VNlRc307i36uGhWuNUC61Iib9ldA34nD7G)

![Image](https://cdn-media-1.freecodecamp.org/images/FdIG9drQMkrMFpYWlxHM4INmxjVtaM8tN53B)

![Image](https://cdn-media-1.freecodecamp.org/images/ezUJoa3dZv6IUhS-QKYc6jWGiBc6apr12efj)
_Same icon, different meanings: “Compose” in the Gmail and Inbox apps, “Edit” in the Snapseed app_

The floating action button was intended to be a great way for users to access a primary action. Except it isn’t, because icon-only buttons tend to be mystery meat.

More on floating action buttons:

[**Material Design:**](https://medium.com/tech-in-asia/material-design-why-the-floating-action-button-is-bad-ux-design-acd5b32c5ef)  
[**Why the Floating Action Button is bad UX design**](https://medium.com/tech-in-asia/material-design-why-the-floating-action-button-is-bad-ux-design-acd5b32c5ef)  
[_Material Design is a design language introduced by Google a year ago, and represents the company’s bold attempt at…_medium.com](https://medium.com/tech-in-asia/material-design-why-the-floating-action-button-is-bad-ux-design-acd5b32c5ef)

### Strike 3: The New Bottom Navigation Bar

This brings us to the bottom navigation bar, introduced in March 2016.

For bottom navigation bars with 3 views, Google’s guidelines specify that both icons and text labels must be displayed. So far, so good: no mystery meat here.

![Image](https://cdn-media-1.freecodecamp.org/images/YGvSiyZjDEce7u2NuFDrRyW7qS77YeOLOuEx)
_Bottom navigation bar with 3 views: so far, so good_

But for bottom navigation bars with 4 or 5 views, Google specifies that inactive views be displayed as _icons only_.

![Image](https://cdn-media-1.freecodecamp.org/images/D7CeYD631OThLgasrNa4NyDb5HpB60IeJWhF)
_Bottom navigation bar with 4 views: mystery meat_

Remember how hard it was to guess what the floating action button icons mean? Now try guessing a row of icons used to navigate an app.

This is just bad UX design. In fact, the Nielsen Norman Group [argues](https://www.nngroup.com/articles/icon-usability/) that icons _need_ a text label, especially navigation icons (emphasis theirs):

> “To help overcome the ambiguity that almost all icons face, a **text label must be present alongside an icon** to clarify its meaning in that particular context.… For navigation icons, labels are particularly critical.”

That Material Design’s newest UI component condones mystery meat navigation is not only frustrating, but also weird. Why should text labels be shown when there are 3 views, but be hidden when there are 4–5 views?

An obvious answer would be space constraints.

Except tab bars in iOS manage to contain 5 icons, and still display the icon and text label for each of them. So space constraint isn’t a valid reason.

![Image](https://cdn-media-1.freecodecamp.org/images/XuHqU7P7rXUzZjAawfbA89u2Gj12Ll6DBQSh)

![Image](https://cdn-media-1.freecodecamp.org/images/8U5exm475tOlJbYAJW8PJeWECTC-PLX93G00)

![Image](https://cdn-media-1.freecodecamp.org/images/Cv6H3piHbcpMiAYyD7h0Ro1CsMi4tuhXw7ed)
_iOS tab bar in the App Store, Clock and Music apps: 5 icons, all with text labels_

Google either decided that icons can sufficiently represent navigational actions (which is bad), or they decided that aesthetic neatness is more important than usability (which is worse). Either way, their decision worsened the UX of millions of Android users.

### Material Design and Form over Function

When Material Design was launched in 2014, it was to much fanfare. It’s bold, and rides on (and one-ups) the flat design trend. The pairing of vibrant colours and animations make it pretty to look at.

![Image](https://cdn-media-1.freecodecamp.org/images/OLb76CbG4u49bqTlU4WNfUXsIWhcmHQ397no)
_“Make it pretty!” — Material Design designer | [Source](https://www.youtube.com/watch?v=Q8TXgCzxEnw" rel="noopener" target="_blank" title=")_

But perhaps it’s a little _too_ pretty. Perhaps while working on Material Design, the designers got a little carried away.

Time and again, Google’s guidelines for important buttons and bars seem to prioritise form over function. Geometric prettiness was chosen over recognisability in Android’s navigation bar. Aesthetic simplicity was championed in floating action buttons, turning them into riddles in the process. Finally, visual neatness was deemed more important than meaningful labels in bottom navigation bars.

That’s not to say that mystery meat navigation is a Google-only problem. Sure, you can find mystery meat in iOS apps too. But they don’t usually appear in critical navigational controls and promoted buttons. They also aren’t spelt out specifically in design guidelines to be mystery meat.

![Image](https://cdn-media-1.freecodecamp.org/images/If7hVf7dEE1YQkJoUeavMmsb0BbrZ0ttLGyV)
_Speed graph showing the correct (blue) acceleration for animations_

If Google designers could devote time and effort into creating speed graphs for animations, perhaps they could spend a little time to make sure their designs aren’t mystery meat.

After all, an animated mystery button is still less delightful than a static but clearly labelled button.

