---
title: 'Swift vs. Objective-C: The trending up-and-comer vs. the dinosaur'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-22T22:10:07.000Z'
originalURL: https://freecodecamp.org/news/https-medium-com-colin-gabriel-smith-swift-vs-objective-c-5b19add8e2ed
coverImage: https://cdn-media-1.freecodecamp.org/images/1*2WOnhJVoWvnNt6HitAQVNg.png
tags:
- name: Apple
  slug: apple
- name: Objective C
  slug: objective-c
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Colin Smith

  A short history of Swift

  I remember how pivotal it was when Swift was introduced at Apple’s 2014 WWDC (Worldwide
  Developers Conference). It was the talk of the town and all the devs I worked with
  couldn’t wait to try it out. The iOS co...'
---

By Colin Smith

### A short history of Swift

I remember how pivotal it was when Swift was introduced at Apple’s 2014 WWDC (Worldwide Developers Conference). It was the talk of the town and all the devs I worked with couldn’t wait to try it out. The iOS community was buzzing and there was a lot of excitement around the new language.

It was developed in order to carry on some concepts we saw in Objective-C such as extensible programming. But it pushed towards a different approach to coding with the protocol-oriented design and increased safety with static typing.

It was a huge hit and saw its growth sky rocket in the years after introduction. It was the [most loved](https://insights.stackoverflow.com/survey/2015#tech) programming language in 2015, the [second most loved](https://insights.stackoverflow.com/survey/2016#technology) in 2016, the 11th [most popular](https://insights.stackoverflow.com/survey/2017#technology) programming language in 2017, beating out Objective-C, and it also [beat out](https://insights.stackoverflow.com/survey/2018/#technology) Objective-C in 2018.

Swift is also a bet by Apple on [winning over novices](https://www.businessinsider.com/apple-tim-cook-on-swift-2017-2) to become iOS developers. The hope is that new developers will learn the language and use it to build iOS apps. This then increases the ecosystem of the app store. Since Swift is optimized to work with iOS apps, this ensures the apps being written are of high quality.

Swifts popularity only continues to increase, especially for smaller apps and start-ups. The gap between Swift and Objective-C will only continue to grow. The future is bright for this young language.

### A short history of Objective-C

Objective-C is an object-oriented programming language that is a superset of C, as the name of the language might reveal. This means that any valid C program will compile with an Objective-C compiler. It derives all its non-object oriented syntax from C and its object oriented syntax from SmallTalk. It was developed in 1984, so it has had time to mature as a language and is much more stable than Swift.

Most people know Objective-C as the language that is used to develop apps for the iPhone, but the history goes much deeper than that. I’d recommend reading [this article](https://medium.com/chmcore/a-short-history-of-objective-c-aff9d2bde8dd) for a more in-depth look.

### The strengths of Swift

Swift has grown tremendously in popularity for a few key reasons. First off, there are a lot of great development tools Apple has provided to work in conjunction with Swift. One of my personal favorites is the Playground, which is only compatible with Swift. Apple introduced Playgrounds [in 2016](https://developer.apple.com/videos/play/wwdc2016/408/). They were introduced as a way to learn how to code, but I loved them for a different reason.

Mobile development has always had more roadblocks than web development. You need a simulator, you usually need a proprietary Integrated Development Environment (IDE), and you need to set up a whole project just to test some small prototype. In Apple’s case, you also need a developer account. The nice thing about Playgrounds is you get around some of this. You do need Xcode or the Playgrounds app, but that is all. And you can get started with coding and compiling your code right away.

Yet, another huge advantage of Swift is the fact that it is open source. If you have ever wondered how a programming language worked under the hood, then you can [go see for yourself](https://github.com/apple/swift)! This is a great way to understand the programming language you work with daily on a deeper level.

An honorable mention goes to a nice utility only available to Swift, the [Swift Package Manager](https://swift.org/package-manager/). The Swift Package Manager is simply a [dependency manager](https://devopedia.org/dependency-manager) that is integrated with the Swift build system. It isn’t a game changer by any means, since CocoaPods and Carthage were doing this job a long time ago, but it’s another solution available if needed.

A lot of evidence here supports the fact that Apple is doing a lot to make Swift more desirable as the programming language of choice for iOS developers. They are creating nice utilities and auxiliaries to entice people to start using the language. This shows that Apple is pushing for Swift in full force.

### Language features

Let’s get into some of the details of the language itself. Swift is safer due to its static typing and the use of optionals. In Swift, if your code requires a string, the features of Swift will guarantee that your code gets a string and not another type, such as an int. This of course depends on if you’re using the language as it is intended and not force unwrapping everything.

Another great feature of Swift is its syntax. Especially compared to Objective-C. The best word to describe the syntax would be “succinct”. There is no need for semi-colons, calls to self or parentheses around if statements. It feels like you are skipping a lot of things that you don’t really need anyway. It can make the process of typing a lot of code “flow” better.

Some people say this leads to development velocity improvements, but I wouldn’t exactly say that myself. The continual need to unwrap objects to comply with Swifts type-safety offsets the development gains that come with the succinctness.

Swift also has a lot of great control flow options with guard, if-let, advanced switch statements, repeat-while and defer. I like all the different options because it lets people control the flow of their code in a way that makes sense to them. A lot of people hate defers but love guards and vice versa. It doesn’t really matter what you like or dislike, but the options are there and you can code in the way that feels best to you.

I can’t forget all the functional programming features such as filter, map and reduce. This is great for handling collections and comes in handy quite often.

### The weaknesses

Swift is a young language, and with that, comes some shifting. The migrations between versions are simply a pain. At a small company, the migration tool provided by Apple can be helpful and cover most cases. It becomes less helpful the more code you have. It’s even worse if your codebase contains both Objective-C and Swift code that interoperate.

At my last company, the migration effort took a dedicated group a whole weekend to do. They had to do it on the weekend so that they wouldn’t run into merge conflicts from other devs pushing code. This was incredibly painful for everyone involved.

A reason for these migrations is the fact that Swift [isn’t ABI stable](https://theswiftdev.com/2018/11/06/swift-5-and-abi-stability/). That means newer versions of Swift cannot work with older versions of Swift. That also means that the language cannot be packaged with the OS. This is a big deal for companies with large apps that actively combat app size because Swift is being bundled with the app and increasing the size.

Another issue is that Swift does not play well with Xcode. Xcode feels very choppy when working with Swift and autocomplete [simply doesn’t work](https://www.reddit.com/r/iOSProgramming/comments/8o1kbt/help_with_xcode_autocomplete_does_not_work/) sometimes. This is strange given how hard Apple is pushing Swift. You would think that they would want make the experience of using Swift with Xcode a delight.

Swift also has problems with string handling, see the code example above. It is clunky as hell. In your day to day, this isn’t too bad. Where this comes into play the most is during interviews. Unfortunately for Swift devs, interviewers love asking questions that involve string manipulation. This is compounded by the fact that the way strings are handled has changed between versions of Swift.

### The strengths of Objective-C

Objective-C is a highly dynamic, object oriented language. It is dynamic to the point that you can swap out method invocations at runtime using techniques like [Swizzling](https://nshipster.com/method-swizzling/). It is able to do these kinds of thing due to its message sending paradigm. This lets objects send messages to other objects at run time to determine the invocation of the method being called.

In practical purposes, what does this mean? Well, one big advantage is adaptability at runtime. This means accessing private APIs or doing things like mocking objects at runtime become possible. This can be especially useful when it comes to unit testing. Libraries like [OCMock](http://ocmock.org/swift/) make this even easier and allow for very elaborate test set ups. Having good unit tests will make your app more stable and reliable.

Speaking of stability, Objective-C has been around for a long time which makes it a very stable language. With Swift, you’ll run into bugs that are [pretty surprising](https://github.com/apple/swift/pull/21727) and would be disruptive to the stability of your app. In the example I linked above, this crash would be caused by the actual language you are using to code your app, not due to any error created by the code you wrote. This can be frustrating.

The last point, which is more important to certain companies, is compatibility with C and C++ libraries. Being that Objective-C is a superset of C, it is easy to use C and C++ code with Objective-C. You can even use Objective-C++ if you feel so inclined. This is important if your are dependent on third party C and C++ libraries.

### The weaknesses

The first main complaint I hear about Objective-C is syntax. I started my professional career using Objective-C so I have no issues with it. It is verbose and a bit unconventional with the use of square brackets. But opinions on syntax are just that, opinions. I figured I would list this point though since it is one of the first things that comes up when you mention Objective-C.

One thing I do agree with though is that block syntax is frustrating. [There is even a website](http://goshdarnblocksyntax.com/) dedicated to decoding the mysteries of blocks in Objective-C. I actually use this website pretty often as a reference.

The biggest issue Objective-C faces right now is the fact that one day Apple may drop support for Objective-C with Cocoa and other common libraries used to create iOS apps. Since Objective-C is primarily used to create iOS apps, this would be a death knell for the language. It also means that newcomers to the iOS community are afraid to commit to learning Objective-C right now since it may no longer be used in the future.

Let’s get back to the language itself. It is prone to having hard to debug issues due to the dynamic nature of the language. The ability to send messages to nil and not crash on top of the lack of strict typing are some examples of things that lead to these hard to debug issues.

Objective-C does not hold your hand when it comes to these things either. Though it is nice that the app doesn’t crash when you send a message to nil, it may put your app in a weird state. It is very hard to debug issues like these. The fact that Swift has strict typing and the use of unwrapping optionals prevents these things at compile time.

### Should I learn Swift or Objective-C?

The answer for most people will be Swift. Apple is clearly pushing Swift as the language of choice for its iOS application development community. Swift will only continue to become more performant as ABI stability is introduced and Swift becomes packaged with the OS itself.

If you’re looking to get a job as an iOS developer, Swift will be the language you want to learn. Most startup to mid-level companies will have their iOS apps written completely in Swift. This means you’ll be able to apply and interview for more jobs if you learn Swift.

Even at larger companies where Objective-C is still used heavily, interviews can still be done in Swift. So you can learn Objective-C once you join the company and not worry about burdening yourself with more things to learn before the interview.

You will want to learn Objective-C if you are already working at a start up or mid-level company and want to jump to a larger company. Skills with Objective-C will give you specialized knowledge and an edge over other interview candidates.

_Liked what you read? Take a look at some of my other articles:_

[Tips for your first tech interview.](https://medium.com/@colin.gabriel.smith/killing-it-during-your-first-tech-interview-16ce13f9d0ce)

[Starting a tech career from nothing.](https://medium.freecodecamp.org/how-i-went-from-stuck-and-hopeless-to-making-my-tech-career-dreams-come-true-d1fcf52c0650)

[Should you get a computer science degree?](https://link.medium.com/rCnf6bajBT)

