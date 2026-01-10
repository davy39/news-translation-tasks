---
title: 'Progressive Web Apps vs Accelerated Mobile Pages: What''s the Difference and
  Which is Best for You?'
subtitle: ''
author: Oleh Romanyuk
co_authors: []
series: null
date: '2020-01-07T14:00:00.000Z'
originalURL: https://freecodecamp.org/news/pwa-vs-amp-what-is-the-difference-and-how-do-you-choose
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/PWA-vs-AMP.png
tags:
- name: AMP
  slug: amp-tag
- name: mobile
  slug: mobile
- name: mobile app development
  slug: mobile-app-development
- name: PWA
  slug: pwa
seo_title: null
seo_desc: 'Do you understand what PWAs and AMPs are, and which might be better for
  you? Let''s have a look and find out.

  So many people own smartphones these days. This opens up endless opportunities for
  a business - opportunities which, however, are immediately...'
---

Do you understand what PWAs and AMPs are, and which might be better for you? Let's have a look and find out.

So many people own smartphones these days. This opens up endless opportunities for a business - opportunities which, however, are immediately challenged by the immense number of competitors in the mobile software market. 

Mobile apps are surely more convenient than web or desktop platforms. Yet, they are not the most comfortable option that the industry offers.

To hit the highest level of user satisfaction and to outrun competitors, inventive people opt in favor of progressive web apps (PWAs) or accelerated mobile pages (AMPs).

What are these things, and how should you choose the best option? Let’s consider each one-by-one by going through these simple questions:

1. What is a PWA?
2. What is an AMP?
3. How are they similar?
4. How are they different?
5. Why PWAs are better than web pages
6. Why PWAs are better than native mobile
7. Why AMPs are better than web pages
8. Why AMPs are NOT better than native mobile

## 1. What Is a PWA?

A progressive web application, or PWA, unites the advantages of both web and mobile apps into a single software product. As [<ins>Google</ins>](https://developers.google.com/web/progressive-web-apps) declares, PWAs are “user experiences that have the reach of the web and are reliable, fast, and engaging”. It is a technology that lets you use a website as if it was a native app.

[<ins>Twitter</ins>](https://twitter.com/?lang=en) is one of the major companies using PWAs. To install the app, you open the web version on your phone and add it to your home screen. When you open Twitter from the home screen icon, you will be opening it as a progressive web app.

![PWA](https://images.ctfassets.net/6xhdtf1foerq/1TGtQag89baQtjFwQFRG1t/29cacc2916819498d669921833c88ceb/8-min.png?fm=png&q=85&w=1000)

### Fundamentals

PWAs are a highly responsive and easily shareable solution, which can work offline. They store HTML and CSS files in the browser cache and archive them with service workers. This makes it possible to use the web page offline. Service workers are one of the three essential components of a PWA, along with the manifest file and a secure protocol HTTPS.

**Service workers** are JavaScript code components which play the role of a proxy between the network and the browser. 

When you open a web page for the first time, service workers store the necessary data in the browser cache. When you open it for the second time, service workers retrieve this data from the cache even before the app checked network availability. 

Not only do they provide the ability to work offline but also they greatly boost the response time. Service workers also manage push notifications.

**The manifest file** is a JSON file containing all the information about your app. For instance, it contains data about the home screen icon of your PWA, its short name, color palette, or theme. 

If you are using the Chrome browser on an Android phone, the manifest file will trigger the automatic installation of the PWA onto your phone.

**The secure HTTPS protocol** is an absolute must if you develop a progressive web app. While service workers make the very concept of a PWA possible, they are vulnerable to network errors or breaches. Service workers can intercept network requests and modify responses. To ensure data security and network security, the secure protocol needs to be used.

### Success stories

Twitter is not the only company that has benefited from PWAs. Check out these [case studies](https://developers.google.com/web/showcase/) published by Google to see how this technology helped popular businesses succeed. Among these companies are [Pinterest](https://www.pinterest.com/), [Alibaba](https://www.alibaba.com/), [The Weather Channel](https://weather.com/), [Lancome](https://www.lancome.com/), and [The Home Depot.](https://www.homedepot.com/)

## 2. What Is an AMP?

AMP stands for accelerated mobile page. It's a mobile-friendly web page, which is designed to be loaded instantly. It is a fast and smoothly loading solution which is developed with the user experience in mind. Introduced as an open-source project, the AMP technology was integrated by Google in February 2016.

In 2016, [The Guardian announced](https://www.theguardian.com/membership/2016/feb/24/todays-release-of-accelerated-mobile-pages-amp) that their platform was now available as an AMP. To help readers see how it worked, they displayed the same article both as [a web version](https://www.theguardian.com/us-news/commentisfree/2016/feb/16/thomas-piketty-bernie-sanders-us-election-2016) and [an AMP version](https://amp.theguardian.com/us-news/commentisfree/2016/feb/16/thomas-piketty-bernie-sanders-us-election-2016). 

There were some differences, but they were insignificant. But what you'd notice right away was how much faster the AMP article loaded compared to the regular web article.

![*By comparing this illustration with the one I included earlier, you could notice an interesting point. A PWA needs to be installed. In turn, you do not need to install AMP. It is accessed via a different like.
](https://images.ctfassets.net/6xhdtf1foerq/1ARjDXZC1yH4p15rxRosIW/e23cf5144729c5985e5a8ac156fb66a6/2.7_billion_people_use_smartphones__1_-min.png?fm=png&q=85&w=1000)
_*By comparing this illustration with the one I included earlier, you could notice an interesting point. A PWA needs to be installed. In turn, you do not need to install AMP. It is accessed via a different like._

### Fundamentals

The idea of AMPs is to reduce the amount of unnecessary content and functionality so that the app displays essential content immediately. The data can be reduced up to ten times. The three essential components of AMPs are AMP HTML, AMP Components, and the AMP Cache.

**AMP HTML** is a simplified version of regular HTML. AMP HTML does not allow some tags and elements of HTML (for example, forms). To understand better what AMP HTML should look like, check out the [required mark-up](https://amp.dev/documentation/guides-and-tutorials/start/create/basic_markup/?referrer=ampproject.org).

**AMP Components** are the scripts that enable you to do without JavaScript. The idea of AMP is to get rid of all JavaScript scripts as make pages load more slowly. 

But this does not mean that your page should do without animations, modified layouts, analytics data, autocomplete suggestions, or ads. There is an extensive [library of components](https://amp.dev/documentation/components/?referrer=ampproject.org) that enable you to implement these and a lot of other features.

**The AMP Cache** is a proxy-based content delivery network which fetches and caches page content. AMP Cache enables you as an app owner to easily introduce page updates. It optimizes and, if needed, modifies the AMP.

### Success stories

The same as with PWAs, companies are often very proud of the business advantages that AMPs offer. Here is a collection of [success stories](https://amp.dev/success-stories/) and case studies of companies that used AMPs and benefited from them. [<ins>Musement</ins>](https://www.musement.com/us/), [<ins>RCS MediaGroup</ins>](http://www.rcsmediagroup.it/), [<ins>CNBC</ins>](https://www.cnbc.com/), [<ins>The Washington Post</ins>](https://www.washingtonpost.com/) are all companies that have implemented or plan to implement AMPs.

## 3. How Are PWAs and AMPs similar?

Both PWAs and AMPs are methods of displaying web pages on mobile devices. Both of them are created to enhance the user experience. 

AMPs and PWAs both help reduce page load time. While AMPs may be slightly more effective in terms of loading speed than PWAs, the difference between AMP and PWA loading times is barely noticeable. 

Both technologies are actively supported by Google. There is [a PWA page on Google Developers](https://developers.google.com/web/progressive-web-apps) and [an AMP page on Google Developers](https://developers.google.com/amp) as well.

There are not a lot of other similarities, but this primary similarity is essential. 

Now let’s see what the differences are. 

## 4. How Are PWAs and AMPs Different?

### Appearance

By using a PWA you do not feel like you are using a web page. PWAs look and feel like a mobile app.

By using AMPs, you are well aware that you are using a web page because it looks the same.

### Development

In the case of PWAs, the application code is written either from scratch or with some parts of the existing code.

In the case of AMPs, the existing code of a web page is stripped of unnecessary CSS and JS so that the web page loads faster.

### User experience

PWAs offer a much better user experience. They have push-notifications, a home screen icon, and no browser tabs. Also, they are much easier to download and lighter in size than a regular mobile app. PWAs load faster than a regular web version because they are embedded with App Shell. And PWAs can be used when the network connection is down.

AMPs offer a slightly improved user experience since the page loads faster than a regular page. Still, this is the only UX advantage that they offer. Unlike PWAs, AMPs cannot work offline.

### Performance

From an SEO standpoint, AMP wins the competition. Google favors these pages and lists them in the carousel of top stories, which can increase your click-through rate.

PWAs, in turn, do not have a direct advantage for SEO. However, better user experience translates into higher retention rates, which helps you win with SEO.

### Support

PWAs are not supported equally on all devices, so you may find slight inconveniences when they're displayed on iOS. Also, they do not support all the hardware functionalities, such as Bluetooth, NFC, GPS, or accelerometers.

AMPs are supported by all major browsers on all devices.

### Apps they're best suited for

PWAs work perfectly for apps that require user interactions. E-commerce websites, social media, or online learning platforms where the app needs to be responsive and constantly updated can make use of this technology. This is why Twitter uses a PWA, for example.

AMPs are more suitable for platforms with a wall of content, such as online magazines or newspapers. AMPs load content instantly, but the interaction opportunities are limited. This is why The Guardian decided to employ AMPs.

## 5. Why PWAs Are Better Than Web Pages

If you access a web page on mobile, you will have to deal with browser tabs, slow loading times, and annoying pop-ups. If your device has a relatively small screen or a slow network connection, surfing the web on it becomes unbearable.

This problem is solved by progressive web apps. In a few clicks, you install the app on your phone and get down to using it. No need to type a link, no browser tabs, and no pop-up screens. The app works fast, and it does work if the network connection is down.

Alright, the benefits of this solution are evident, but it seems like native mobile apps could work perfectly instead. No, they would not. Let’s see why PWAs are better than native mobile apps.

## 6. Why PWAs Are Better Than Native Mobile Apps

To use a native mobile application, you have to find it in the App Store or Google Play catalogs. Then, you have to wait for some time to download it. You might not have enough free space on your device, so you'll need to find some room.

In turn, PWAs are installed and ready to use in seconds. The file size is small (although it's bound to increase while you are using the app and it is caching). Still, the size of the cached data depends on the amount of free storage you have on your device.

As you can see, PWAs seem better than a web or native mobile app. But you should understand that this solution is not universal. Check out my recent article on [PWA vs Native](https://keenethics.com/blog/progressive-web-apps-vs-native-which-to-choose-and-when) to learn when a native app is a better choice than a PWA.

## 7. Why AMPs Are Better Than Web Pages

As mentioned above, web apps are slow and inconvenient, especially when accessed on mobile devices with small screen size or underpowered hardware.

By getting rid of all the web components that are unnecessary for a good user experience, accelerated mobile pages solve this problem. AMPs perform 4 times faster and use 10 times less data than regular web pages.

## 8. Why AMPs Are NOT Better Than Native Mobile

Unfortunately, AMPs cannot be a complete substitute for native mobile apps. They cannot be installed on the home screen, they still include browser tabs, and their functionality is limited to some basic stuff.

But for an online newspaper or for an informational website, such as [WebMD](https://www.webmd.com/), it is better to use AMPs rather than a native mobile app. These do not require any additional functionality for displaying page content.

## To Wrap Up

Both AMPs and PWAs are powerful technologies. To sum up the results of our initial question - PWAs vs AMPs: 

* AMPs will be easier, faster, and cheaper for you to develop 
* PWA will offer more benefits.

Just remember - neither of them is a universal solution, and neither is a panacea. Even using AMPs and PWAs together may not meet all your demands. Sometimes you may need to choose more conventional types of software. 

If you are still not sure what to choose, our specialists share <ins>[four questions to understand if you need PWA](https://www.freecodecamp.org/news/four-questions-to-understand-if-you-need-pwa/)</ins>. In short: _We believe that progressive web apps are the future. Accelerated mobile pages are just too simple and limited in functionality to compete._

## Do you have an idea for a project?

My company KeenEthics is experienced in both AMP and [progressive web app development](https://keenethics.com/tech-apps-progressive-web-apps). If you are ready to change the game and start your project, feel free to [get in touch](https://keenethics.com/contacts)_._

## P.S.

The original article posted on KeenEthics blog can be found here: [PWA vs AMP:  What Is the Difference and How Do You Choose?](https://keenethics.com/blog/pwa-vs-amp)

