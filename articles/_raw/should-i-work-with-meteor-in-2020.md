---
title: Why You Should Work With Meteor in 2020
subtitle: ''
author: Oleh Romanyuk
co_authors: []
series: null
date: '2020-04-24T19:40:56.000Z'
originalURL: https://freecodecamp.org/news/should-i-work-with-meteor-in-2020
coverImage: https://www.freecodecamp.org/news/content/images/2020/04/work-with-meteor-in-2020.png
tags:
- name: JavaScript
  slug: javascript
- name: Meteor
  slug: meteor
seo_title: null
seo_desc: 'Meteor, an allegedly dead development platform, is still alive and can
  bring massive value to your everyday coding experience.

  Meteor appeared at the beginning of 2012, rocking the web development world. The
  possibility of bridging the gap between th...'
---

_Meteor, an allegedly dead development platform, is still alive and can bring massive value to your everyday coding experience._

Meteor appeared at the beginning of 2012, rocking the web development world. The possibility of bridging the gap between the server and client sides of a particular website or web app was genuinely tempting. 

Many experts thought that this capability alone should have turned the platform into a mainstream industry standard. Nevertheless, eight years later, many people claim that Meteor is dead.

Is that so? And is there any rational justification for learning Meteor? This article will give you a definitive answer.

## **Meteor is Dead! Long Live Meteor!**

Many developers believe that Meteor is dead. The popular explanation is simple: being introduced in 2012, it already had a promising set of features in 2015 but failed to extend them significantly. 

Some of you might have even heard of the problems with the funding of the development team, too. For many people, this fact alone is enough to forget about the platform once and for all.

However, the reality is much more optimistic than it may seem. Today, the developers of Meteor receive stable funding from Tiny, one of the most reliable investment funds in IT. The version history also shows that the development platform is far from being dead, with the most recent iterations having a proud 1.10.1 designation released in February 2020. 

Thus, if you have always secretly liked Meteor but were afraid to choose the platform due to the constant reports of it being dead, now is the perfect opportunity to hop onto the hype train.

_The reports of Meteor's death are greatly exaggerated, and the possibility of its success is greatly underestimated._

## **Unprecedented Simplicity: The Key Features of Meteor**

Now that we have clarified the status of Meteor, it is time to describe some of its killer features. Meteor is undoubtedly among the most feature-rich and, at the same time, easy-to-use JavaScript frameworks today.

### **Killer Feature 1: Unified Client and Server Development**

Meteor, as we have mentioned before, is notable for its ability to bridge the gap between the server and client sides of any project. Thus, every aspect of your website can be developed solely via JavaScript. 

The benefits of this feature are boundless in the modern development world, and are valuable for both fledgling and the experienced developers.

Above all, this approach allows developers to create projects without experience with other programming languages.

Thus, a talented but inexperienced JavaScript programmer can easily maintain several Meteor projects without any problems. Experienced developers can go even further, maintaining whole ecosystems of services and products via the Meteor platform. 

Consequently, the adoption of Meteor in your company can be an extraordinary boon for all involved parties.

* Your programmers will be able to develop more and spend less time on the exhausting process of learning additional frameworks and programming languages.
* Your customers will enjoy lower pricing on services.
* And you will reap higher profits after the adoption of the framework.

Independent developers can also be the major benefactors of the development platform today. After all, the ability to use only one language for personal programs will give you an opportunity to take on more freelance projects.

### **Killer Feature 2: Transforming Web Applications into Smartphone Programs**

Every company that develops a specific web application seeks to have a smartphone version of its product. The benefits of such a strategy are rather obvious: after all, everyone has an Android or iOS phone today. 

However, the businesses that seek smartphone versions of their apps often face the problem of massive development costs. The mobile versions of their web apps are often recreated from scratch. 

If they are lucky, this process might only involve the client-side platforms. However, smartphone development frameworks are so divergent that sometimes both the client and the server have to be extended.

We are quite sure that you have seen frustrating situations in which certain web apps only have iOS or Android clients for smartphones. The lack of unity regarding frameworks is the main culprit in this case.

Meteor offers an elegant and extensible solution to this problem. Due to the potent integration of Meteor with Apache Cordova, you can quickly turn your web application into a smartphone app without any significant investment. 

On the purely technical side, such a transition is possible due to the embedded container capabilities of Meteor and Cordova. All you would have to do is insert your web app into a pre-developed smartphone container.

Another critical design choice is the approach Meteor takes with data. Meteor uses data on the wire – the server doesn't send HTML but data, which is then rendered by the client. If the design of your web app is already touchscreen-friendly, you can immediately push your new program into the App Store or Google Play Market with Meteor.

If that is not the case, all you would have to do is slightly adjust the design using the JavaScript language. Essentially, the process would be similar to developing a mobile version of a website.

Once again, such an approach will save you unprecedented amounts of time and money. Instead of having to hire some dedicated smartphone developers, you will be able to fully concentrate on your web apps. This feature is also vital from a purely aesthetic standpoint. Meteor is one of the best tools when it comes to making the design of your products uniform.

The use of a unified platform will help you establish a professional standardized look in all business spheres.

### **Killer Feature 3: Real-Time Updates**

Meteor is also capable of real-time updates, or so-called "full-stack reactivity." The changes you make immediately appear across all databases and style templates. In this way, you would be immediately able to see critical bugs and double check the features without having to tediously update web pages and certain programs.

This feature is of vital importance when it comes to large teams. The immediate updates are visible to all team members, creating a perfect environment for collaborative development. Ultimately, your web apps and smartphone programs will significantly benefit from this feature as it makes bug fixing incredibly simple.

Without going into details, one way of implementing the feature is a publication/subscription functionality.

```js
// Code on the server side
const MyAwesomeData = new Mongo.Collection('myAwesomeData');
Meteor.publish('myAwesomeData', () => {
return MyAwesomeData.find() 
})
```

It creates a publication for everything in the collection `myAwesomeData`. This publish function is requested whenever a client subscribes to it. So, let's create a subscription.

```js
// Code on the client side
Meteor.subscribe('myAwesomeData')
```

Now, all the subscribers will receive updates whenever a publication is requested. Also, we can receive data using a specific parameter.

```js
// Code on the server side
Meteor.publish('myAwesomeData', (userName) => {
return Comments.find({ userName: userName })
})
```

The last piece of code retrieves data using a specific user name:

```js
// Code on the client side
const userName = 'Jack Sparrow'
Meteor.subscribe('myAwesomeData', userName)
```

### **Killer Feature 4: Easy Package Management**

Often, the deployment of modified versions of development frameworks requires a significant expenditure of time and resources. Meteor, however, is extremely user-friendly in this regard, offering some of the best package management tools on the market.

Today, the community of the Meteor developers maintains a gargantuan database of extensions on the [AtmosphereJs website](https://atmospherejs.com/). Some of the popular extensions include tools for embedding ReactJS and Vulcan Bootstrap.

To install an Atmosphere package, you simply run the following command `meteor add nameOfThePackage`:

```js
meteor add react-meteor-data
```

And to delete a package:

```
meteor remove react-meteor-data
```

To import and start using it in code, you should use the "meteor/" prefix:

```js
import { useTracker } from 'meteor/react-meteor-data';
```

More information can be found here: [https://guide.meteor.com/using-atmosphere-packages.html#peer-npm-dependencies](https://guide.meteor.com/using-atmosphere-packages.html#peer-npm-dependencies)

This feature is especially impressive considering its simplicity. The installation process only requires a set of simple commands that almost any advanced Windows or Linux user should already be comfortable with.

Even if you are an absolute beginner, you should have absolutely no problems with setting up a basis for even the most complex programs.

Thus, any person can swiftly create app prototypes and make them feature-rich by using this robust library of extensions and the advanced package management tools provided by some of the Meteor developers and the active community that surrounds the framework.

### Killer Feature 5: Extensive Learning Resources and Documentation

One of the key problems of many open-source projects is the complete lack of proper documentation. This problem led to the death of countless promising projects as outside developers were often forced to essentially reverse-engineer their features.

Do not worry – Meteor is unlikely to fall victim to this problem. After all, the website of the platform has a powerful set of tutorials for beginners and a whole subsection is dedicated to documentation.

We recommend these resources to both the beginners and the advanced users.

If you are new to web development, Meteor tutorials will help you create your first web apps (one of the highlights includes a Whatsapp clone).

If you are an advanced developer, the tutorials will quickly teach you the basics of Meteor. After that, you will just need to check the documentation from time to time to resolve some issues.

### Killer Feature 6: Active Community           

If you fail to find information on the Meteor website, you can always resort to the robust forums.

We have spoken extensively about the death of Meteor in the first section of this article. Few facts defy this claim as much as the community of Meteor users.

As the massive extension library of Meteor proves, the framework receives active support not only from its developers but also from the community. 

At the time of Meteor's presumed death, the interest from developers regarding the platform was seeing unprecedented growth. Consequently, the framework now has an incredibly passionate user base which is always ready to troubleshoot your problems. 

Many people (including myself) know that Meteor’s community is among the nicest on the Internet. You are unlikely to meet any hostility there, and many active members are eager to help newcomers.

Since Meteor developers have received a significant financial boost from the Tiny Investment Fund, this community is likely to grow even more. Thus, your adoption of Meteor is likely to be very smooth as countless developers will be be ready to assist you.

![Image](https://lh6.googleusercontent.com/9eJoT3zwUJddKFYwa2-6Bu9cVNiZqECb3JrcYw3w3--9D8Y0uqqpOAwITp9mVLDQfZtgw3j5wVSTd6eK6q92Zrh-751kyO37gePsWnuAMb81XWKrOWI3Bu1lJLhqH0sNzXxG0aI)
_Info-graphic. The Popularity Levels of Meteor. Courtesy of BuiltWith Trends Service. Accurate as of April 2020. Link: [https://trends.builtwith.com/framework/Meteor](Infographic 1. The Popularity Levels of Meteor. Courtesy of BuiltWith Trends Service. Accurate as of April 2020. Link: https://trends.builtwith.com/framework/Meteor.)._

## **Conclusion: So, Should You Learn Meteor?**

The short answer is simple: yes, undoubtedly.

Knowledge of the Meteor platform is the perfect addition to any developer's portfolio.

* If you primarily develop with JavaScript, the platform will help you or your company cut time expenditures on creating separate client and server projects.
* If you are an independent developer who uses C# or Ruby, Meteor can be a perfect entry point into JavaScript development. It will allow you to create independent web app projects with one programming language.
* If you are an absolute beginner, the platform will help you create your first well-functioning apps after just a few weeks.
* If you want to establish a startup, Meteor can be a perfect starting point for quickly creating a powerful prototype of your future web app. More importantly, the tool is robust enough to make any transition to other platforms unnecessary after prototyping.

Essentially, with Meteor, only the sky is the limit. Modern development is becoming more and more web-centric. Meteor perfectly reflects this trend, offering an all-encompassing platform for web developers. 

By using it, you will be able to create a seamless integration of web and mobile apps, both of which are the future of consumer-centric computing.

## **Do you have an idea for a JavaScript project?**

My company KeenEthics is an early adopter of the [Meteor framework](https://keenethics.com/services-web-development-meteor) and a well-established JavaScript company in general. In case you have a promising project in mind, feel free to [request an estimate](https://keenethics.com/contacts?activeform=estimate)_._

If you have enjoyed the article, you should continue with [What Are the Advantages of Node.JS?](https://keenethics.com/blog/what-are-the-advantages-of-node-js) and [Angular vs React: What to Choose for Your App?](https://keenethics.com/blog/angular-vs-react-what-to-choose-for-your-app)

