---
title: How to find out if Ionic is the right choice for your project
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-21T17:00:50.000Z'
originalURL: https://freecodecamp.org/news/is-ionic-the-right-choice-for-my-project-f15774303956
coverImage: https://cdn-media-1.freecodecamp.org/images/0*X51csfCLWEo2IsQl
tags:
- name: Angular
  slug: angular
- name: JavaScript
  slug: javascript
- name: mobile app development
  slug: mobile-app-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Simon Grimm

  Ionic has been around for quite some years. With the latest release of version 4,
  it has become an even better option for developing hybrid apps than it was already.
  Still, there are drawbacks and scenarios where Ionic might not be (or...'
---

By Simon Grimm

Ionic has been around for quite some years. With the latest [release of version 4](https://blog.ionicframework.com/announcing-ionic-4-beta/), it has become an even better option for developing hybrid apps than it was already. Still, there are drawbacks and scenarios where Ionic might not be (or should not be) your first choice.

In this article, we’ll take a look at questions you should answer **before picking Ionic** for your next project. In the end, the result might very likely still be Ionic, but there are other great alternatives as well.

Software Development is no competition and we don’t need a winner here. We can accept that there are many great frameworks in this world. Each has its unique strengths and tradeoffs. You can embrace a great framework for your job or spend time explaining why framework x is so bad. The decision is up to you, so choose wisely how you want to spend your time.

Be aware that the term **Hybrid Apps** can sometimes still be a red flag for decision makers. If they are not convinced after uncovering the [10 Hybrid Myths](https://devdactic.com/myth-hybrid-development/), this article will give them a clearer path.

If you’ve already fallen in love with Ionic or want to learn more about it, you can take the next step with my exclusive Ionic learning platform [the Ionic Academy](https://ionicacademy.com/). It offers courses, projects, and an awesome community to help you become an Ionic Developer.

### What’s your project?

In the beginning, there’s an idea or task that will become a project later. At this stage, you need to find out what **platforms** you want to support. You also need to decide what are your project’s biggest **priorities**. If you develop something completely new, it’s easier to pick something new. It is much harder when you already have requirements based on a legacy system.

First of all, _where do you want to offer the app_? Inside the native app stores, on the web, as a PWA or even as a desktop application?

Your answer will be one or a combination of these. If you are targeting many platforms, Ionic would be a good choice.

When you only need a web application, create for example a pure Angular project. If you only need desktop apps, use Electron or something completely different. (_This is not my main area of focus, really_).

But once you see that you need to target mobile and web, Ionic offers a great way to keep your code in a code base with one language. At this point, it doesn’t matter if you need a native app or PWA, because you can get both with Ionic.

The result of using a cross-platform framework is potentially higher when you use it as a cross-platform tool. This always means it’s not going to be 100% like doing it with the inherent approach of the respective platform. You can get close to it to a certain degree while your cost decreases.

Which brings us to the priorities of the project. If your priority is to have the best 3D visuals an app has ever seen, stop reading here. That’s not a use case for Ionic but something like [Unity](https://unity3d.com/).

If your priority is to offer your customers a solution on all their preferred platforms, **Ionic can help you to get there more quickly**. Because you can build your one code base into many different forms in the end. You are more flexible and able to target a variety of platforms.

In the end, every project has a budget and timeline. This means, **it’s a business decision** based on many variables you can sometimes only estimate upfront. Do your job, outline what’s important and where you want to be. This will give you the first indication of whether to use Ionic or not.

### What are your team members’ skills?

When you have a team of 5 non-developers that are just starting to learn what an Array is, there’s no big difference between picking framework a or b. If you have a team of 5 Angular developers, the likelihood of picking Ionic suddenly increases a lot.

Although you should (of course) always try to use the best tool to deliver the best possible result for your project, it doesn’t mean that this selection makes the most sense or has the highest **business value**.

If you have experienced developers with a lot of C# knowledge, why not try something like [Xamarin](https://visualstudio.microsoft.com/xamarin/)?

If all your team knows React, why not use [React Native](https://facebook.github.io/react-native/)?

![Image](https://cdn-media-1.freecodecamp.org/images/dllUJaoFXI6TMBOz-ca5azVGXSjQqg7Vys1D)

As I said in the beginning, there are many great frameworks available. Each with their own unique approach. And if you can benefit from the experience of your developers, you will get started a lot faster. Perhaps also get a better result with something they would have to learn from ground zero.

When you have a handful of web developers with basic JavaScript skills, **Ionic is the perfect framework to transition to mobile apps**.

Also, in case you have a development team of 100 native developers, chances are high you should go native. It seems like your business focus is on developing the best possible app for your end-user.

But when your team is not at that stage (yet?) evaluate your previous skills. Keep in mind the target platforms of your project from the first step because not all of the mentioned framework can **deliver the same result across those platforms like Ionic does**.

Combine those 2 elements to see what framework could be a match!

### Benefits You Get with Ionic

Once you decided that Ionic might be the right fit, it’s time to look at the potential upsides of using it.

#### Codebase

As already mentioned, your result is **one codebase** which you can use to **build for multiple platforms**. That means the initial development time is faster. Also, further maintenance and updates are easier to ship as it only requires changes in one project.

While this sounds awesome, it’s never going to be 50% (or more) of the development time compared to creating x projects for each separate platform you target. Sometimes you just need to take care of special behaviors so you need to add clauses like:

```
if (this.plt.is('ios')) {  // do ios Stuff}
```

```
if (this.plt.is('android')) {  // do android stuff}
```

Ionic is already doing their best to simplify this process with f[a project called Capacitor](https://capacitor.ionicframework.com/). This defines one API that will work both on the web and with native SDKs. At the time writing, this it has not yet reached a stable version, but looks **very promising for the future**.

#### Platforms

Because Ionic is betting on the web, Ionic apps can run almost anywhere today. An Ionic 4 project is a web application that gets packaged into the right container for a specific platform.

On the web, this means it can be deployed directly as it is. As a PWA, you need to comment in a snippet and it’s ready. For the native app stores (iOS/Android), [Cordova](https://cordova.apache.org/) will package your application. Cordova makes the underlying SDKs and device features available. And for desktop, you can use [Electron](https://electronjs.org/). It is already used by applications like Visual Studio or Slack.

#### UI Elements

If you want to explain Ionic very (very, very) simply, it’s a **great UI library** of elements. Especially with the version 4 update, Ionic moves towards a direction where it can be easily added to any project. Its components are now web components created with their own tool [Stencil](https://stenciljs.com/).

While Bootstrap was and still is great for the web, having platform-specific components is almost a must-have today if you want your users to enjoy your app.

_Ever seen an Android-designed iOS App?_

It either never gets through the Apple Submission guidelines check or feels just wrong when used.

Ionic automatically uses the styling based on the platform where the app is running. While they are already looking good out of the box most of the time, **everything can be customized** to meet your expectations. It’s not like you have to live with predefined colors or anything. There are standard values to help you get started faster.

#### Tooling & Development Flow

If your development environment sucks, your productivity decreases. If you have the right tools and feel comfortable with your flow, your productivity will likewise be a lot higher.

With Ionic 4 you get the power of the Ionic CLI of previous releases. Plus you can also use the [Angular CLI](https://cli.angular.io/) without any problems right inside your project!

This means bootstrapping projects, adding new files, and creating the right structure becomes a lot easier.

Also, compared to native development, the **live reload** of your app is something those developers can only dream of.

Combined with the additional safety of [TypeScript](https://www.typescriptlang.org/) and a great editor like [Visual Studio Code](https://code.visualstudio.com/), developing Ionic apps becomes less a job and more pure fun.

#### Support & Community

While you expect great support and a friendly community from all famous frameworks, it’s not always going to be like you imagine it. Because the main focus of Ionic is still Angular, you can not only get help from fellow Ionites but also benefit from **the whole Angular community**.

And once more users of other frameworks start to use Ionic, the size of the community will increase more and more over time.

If you are looking for another great Ionic community, you can find a friendly place inside my [Ionic Academy](https://ionicacademy.com/).

Also, looking up something inside documentation can be quite painful. Ionic makes delivering an awesome experience in this area a high priority. Check out there [beautiful redesigned Ionic 4 docs](https://beta.ionicframework.com/docs/) to see what I mean. It’s definitely more than you can expect from an open source framework!

#### Ionic Pro

Although **Ionic is open source and free**, you can add another set of tools by using [Ionic Pro](https://ionicframework.com/pro). This paid service adds additional functionality like visual App creation with the creator, improved deployment process (live app updates), error monitoring or testing channels.

While none of these is a must have, it’s an amazing suite of tools that you might want to have if you can afford the price.

For enterprise teams, the benefits will clearly pay off. For smaller companies that take their apps seriously, it’s something they should think about to [increase the productivity of their development team](https://devdactic.com/efficiency-ionic-pro/).

### Areas of Improvement within Ionic

Until now I’ve blown the trumpet quite hard for Ionic. This is because I’ve fallen in love with it over and over again in the last years. But of course there are drawbacks to every framework, and Ionic is no exception.

#### Performance

The biggest concern against cross-platform apps will always be the performance. Yes, Ionic apps run inside a Webview. There are no real native elements. They will always be inside this container and at least one level above real native apps.

On the web in general, that’s not an issue, as Ionic apps are a website like everything else.

As a native application, this can become a pain point especially **if a bridge to a native functionality is the bottleneck** that keeps hanging and slows down your app. Again, if your top priority is the best performance ever seen by a mobile application, you might want to go full native.

Also, the usage of JavaScript is super easy, but at the same time there are many areas where inexperienced developers can go wrong which results in slow apps. [Josh Morony has a great article](https://www.joshmorony.com/ionic-framework-is-fast-but-your-code-might-not-be/) on why the code, not the framework, might be the real problem with the performance.

**You can definitely build super performant apps with Ionic.** It’s just easier to mess up with performance than it is with a framework that’s closer to native code (or completely native).

#### Reload

The cool reload was a benefit just some paragraphs ago _and now it’s a drawback?_

To understand it, you need to learn the difference between **live reload** and **hot reload**.

The first is used with Ionic and means your app is updated once you save your code. The second means your app is updated once you save the code **in the exact same state it was before**.

That’s a difference, especially if you are testing your app on a mobile device or simulator where the loading times can really slow down your process.

Of course, this is not a showstopper, but something developers would highly benefit from in the future.

#### Native SDKs

If one of your platforms is a native app, odds are high that you want to use device features or the underlying SDK. While this is not a problem itself through Cordova, it can be painful sometimes.

There are Cordova plugins for almost everything you can imagine. Once you need a very unique feature and discover that the only plugin for this was updated 3 years ago **you know you gonna have a hard time**.

This doesn’t mean it’s the end of the road. At this point, you might have to touch native code that you don’t comfortable with. With Cordova means **we can’t access native functionality directly**.

With other frameworks like NativeScript, it’s a lot easier to work directly with the native SDKs. For Ionic, you currently still need a bridge between.

Maybe this pain point will be removed or decreased once Capacitor is ready for prime time. Until then you must live with what you get or become active by developing your own plugin.

#### And what about the AirBnB and Facebook News?

You might have heard the news of [AirBnB sunsetting their work with React Native](https://medium.com/airbnb-engineering/sunsetting-react-native-1868ba28e30a). You may have heard older news from the Zuck that [betting on HTML5 was the biggest mistake of Facebook](https://techcrunch.com/2012/09/11/mark-zuckerberg-our-biggest-mistake-with-mobile-was-betting-too-much-on-html5/).

These articles create a lot of doubt against the general cross-platform approach.

_Is developing cross-platform still valuable?_

The short answer is: **Yes, more than ever**.

To understand how those companies came to these decisions you would have to truly understand their business and their situation. AirBnB has more than 100 native developers. _How many does your company have?_

If I had a team of 100 experienced natives devs, I guess the last thing I would do is tell them to stop all native work and go for Ionic now.

This means **you shouldn’t be scared by big headlines of big companies**.

The decision for or against Ionic or any framework is based on many factors. Just because one company stops using a tool it doesn’t mean the tool sucks. It was just not the right fit for their needs.

Ionic could be right for your next project or not. Don’t let that decision be based on big headlines, but rather on your own evaluations.

### Conclusion

In this article, we went through many steps to see whether Ionic might be the right fit for your next project or cross-platform app. With the closer Angular integration with Ionic 4, it’s a great choice for any web and mobile project. But it always depends on your business case, priorities, and factors you value!

Don’t fall back into preconceptions you have built and fostered over the years. Try it out for yourself.

If you want to learn how to build great apps with Ionic, check out [the Ionic Academy](https://ionicacademy.com/)!

_Originally published at [devdactic.com](https://devdactic.com/ionic-right-choice-project/) on August 21, 2018._

