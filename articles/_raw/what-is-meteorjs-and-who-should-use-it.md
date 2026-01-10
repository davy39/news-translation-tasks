---
title: A Quick Guide to MeteorJS – What it Is, and Who Should Use it
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-28T23:40:40.000Z'
originalURL: https://freecodecamp.org/news/what-is-meteorjs-and-who-should-use-it
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/meteor-2.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Meteor
  slug: meteor
seo_title: null
seo_desc: 'By Yehuda Clinton

  MeteorJS is a do-it-all framework for making JavaScript applications. If you enjoy
  making websites in HTML, CSS, and JavaScript, then you can use those skills to make
  apps for your PC or phone.

  By default when you do “meteor create ...'
---

By Yehuda Clinton

MeteorJS is a do-it-all framework for making JavaScript applications. If you enjoy making websites in HTML, CSS, and JavaScript, then you can use those skills to make apps for your PC or phone.

By default when you do “meteor create myapp & cd myapp & meteor run”, it serves an HTML/JavaScript web page along with a Node/MongoDB backend (which is unused at this moment).

Nodejs is simply the name for the JavaScript that sits on the server end. Mongodb is the NoSQL (not-only-structured-query-language) database that Meteor uses.

## Let's start a mobile app demo

To get started, you type “meteor add-platform android” and then “meteor run android”. This will run this app on your [plugged in](https://www.xda-developers.com/install-adb-windows-macos-linux/) phone (or [virtual device](https://medium.com/androiddevelopers/developing-for-android-11-with-the-android-emulator-a9486af2d7ef)) using your computer as the server (if you made something in the backend). You can do the same thing with an iPhone using a Mac.

The JS, HTML, and CSS files are intuitively organized within the 'server' and 'client' directories. This is the MVC (model view controller) design pattern.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/mobile-1.png)

The Android and iOS mobile interfaces are handled by Apache Cordova. You won't see it in a basic webapp. However you should definitely be aware if you are using any phone hardware functions.

The basic platform allows you to add on whatever other framework you wish to the back end or front end. Everything from Angular, Express, React and Vue can be installed on top of Meteor. 

Popular CSS frameworks like Material-UI are usually used to ease the design work. However you don’t need to add any other framework at all. Meteor comes with a great [Publish/Subscribe](https://docs.meteor.com/api/pubsub.html) method, [Blaze handlebars](http://blazejs.org/) and user-accounts, and much more.

## Beyond the Demo

Besides the plugins available with "[meteor add](https://atmospherejs.com/)", you also have access to all npm and cordova plugins. You can use "meteor npm install" to access them.

You can even add a desktop platform using [Meteor-desktop](https://github.com/sharekey/meteor-desktop/). This uses the Electron framework. You can then make Windows, Mac, and Linux applications. Hopefully this functionality will be natively supported in Meteor version 2.0.

There has been a healthy community of Meteor developers in different forums since 2012. The documentation at guide.meteor.com is more extensive and clear compared to most frameworks.

Although this may seem to be the perfect shortcut for a new developer, I will warn you: Don't include a package or framework in your project until you are confident you know how it works. 

Meteor is good at integration but it can take extra work to combine different packages. Don't just shop around for a list of packages expecting it will work all together perfectly. 

Meteor is a great tool for a beginner looking to be introduced to the broad scope of app development and the process of building a simple app.

## **Production**

Meteor can, of course, create full production web and mobile apps. It's used by several mid-size and large companies such as Ikea and Workpop. 

For easy development and optimization, you can use [Galaxy](https://www.meteor.com/hosting) hosting. Galaxy will help get you to production without any system administration knowledge required.

If you do have knowledge and time, then you can host it on your own server/VPC. For example, a $5 a month AWS Lightsail instance can host an app with a hundred users.

Self-hosting and building works much the same way as you began the Meteor demo. However, instead of "meteor run" you will be building (meteor build) – your backend into a standard nodeJS app, and your mobile into a [signed APK](https://medium.com/@yehudaclinton/how-to-make-an-android-app-with-meteorjs-62ae5b22623a) or IOS app.

There have been rumors over the years that Meteor doesn't scale well. This has been largely disproved and can be overcome with various techniques.

Meteor security has the typical high standards of a well maintained open-source project. Follow the [security guide](https://guide.meteor.com/security.html) closely and watch out for [noSQL injection](https://medium.com/rangeforce/meteor-blind-nosql-injection-29211775cd01).

## Advantages of Meteor

* A diverse community of contributors gives the framework special resilience and longevity. Most other frameworks are created by a single mega tech company. This could mean that the project will get shelved if they see no return on investment. With Meteor, the direction of its development closely follows its users.
* It's cross-platform. Googles Flutter isn't going to work on Apple's iPhone. Meteor allows you to make all the implementations of your app in one place.
* It's built in MongoDB handlers and there's support for GraphQL.

## Disadvantages of Meteor

* If developers place too much reliance on different pre-built packages they can conflict with one another.
* If you are just making a webapp it might be simpler to use Express.
* You can't make a mobile web-app run as efficiently as with native.

In conclusion, Meteor is an effective framework that can help you cut development time and ease app maintenance.

If you are looking to learn more on how to make Apps in JavaScript, read this new [book from Manning](https://www.manning.com/books/the-joy-of-javascript?utm_source=affiliate&utm_medium=affiliate&a_aid=bootstrap-it&a_bid=e5f7023c&chan=VPN) Publications.

