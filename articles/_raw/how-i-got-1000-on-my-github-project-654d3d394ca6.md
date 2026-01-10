---
title: How I got 1,000 stars on my GitHub Project, and the lessons learned along the
  way
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-10-24T07:12:01.000Z'
originalURL: https://freecodecamp.org/news/how-i-got-1000-on-my-github-project-654d3d394ca6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*GKW7LslZMfOLVbqC4ok1Ow.png
tags: []
seo_title: null
seo_desc: 'By Andrea Bizzotto

  I’ve been an iOS developer since 2012. I started writing open source code, to stop
  re-inventing the wheel and carry over my best code across projects.

  While some of my early projects had gathered some interest from the community, n...'
---

By Andrea Bizzotto

I’ve been an iOS developer since 2012. I started writing open source code, to **stop re-inventing the wheel** and **carry over my best code** across projects.

While some of my early projects had gathered _some_ interest from the community, none of them took off like [**SwiftyStoreKit**](https://github.com/bizz84/SwiftyStoreKit) did.

Before I share the secret sauce that made this possible, let me say one thing:

> I want my code to have an **impact** in the world.

> I want my code to empower developers, so that they can focus on creating great apps.

> If I succeed, all the bug fixes, answered questions and unpaid time I put in will be worth it.

Open source software **has leverage**. My code reaches end-users via multiple apps, and enables fellow developers to be more productive.

**How much leverage?**

According to the [Cocoapods Metrics API](http://blog.cocoapods.org/metrics-api/), **SwiftyStoreKit** [has been downloaded](http://metrics.cocoapods.org/api/v1/pods/SwiftyStoreKit.json) **42302 times** and installed into **1194 apps** as of October 20th, 2016.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aRR-MUwscyB2oEp8imuKgg.png)
_GitHub Traffic page for SwiftyStoreKit (October 20th, 2016)_

_For context, [AFNetworking](https://github.com/AFNetworking/AFNetworking) (one of the top iOS projects) [has been downloaded](http://metrics.cocoapods.org/api/v1/pods/AFNetworking.json) 21,659,973 times and installed into 413,742 apps._

But enough bragging now. ?

My point is that **you** can do this too.

* [**Stay on top of your game**](https://medium.com/@ajithrnayak/stayin-on-top-of-your-game-ios-newsletters-blogs-developers-companies-to-follow-527b859b3bb5#.mml1nu6jc).
* Write your own code and open source it, or contribute [to existing projects](https://github.com/vsouza/awesome-ios).
* **You will grow as a developer** and you can really help and benefit others.
* Doing this is great for your CV. It will make you **stand out** and **land better jobs and clients**.

So, how did I get all the ⭐️⭐️⭐️⭐️⭐️?

### My recipe

1. Choose the right project
2. Make it easy to use
3. **Write the best README you can**
4. Share **in the right places**
5. **GitHub Trending**
6. **Google Search**
7. Keep growing

Let’s look at these points in detail.

### 1. Choose the right project

How do you choose? A good way to start is to **solve a problem you have**. In my case, I needed an in-app purchase (IAP) framework for [one of my apps](https://itunes.apple.com/app/id930804327).

IAPs are a very popular way of monetising your apps in the App Store.

Unfortunately, Apple’s [StoreKit](https://developer.apple.com/documentation/storekit) framework is not exactly the easiest thing to work with:

* Many native APIs to learn, mostly designed in the era of Objective-C.
* Various types of in app purchases.
* Security considerations are very important.
* Testing that your purchase flows are correct is hard.

A lightweight IAP framework to make things easier was sorely needed, so **SwiftyStoreKit** was the right project.

### 2. Make it easy to use

While I have tried some other 3rd party IAP libraries before, not a single one was as simple as I had hoped for.

I started building **SwiftyStoreKit** when Apple released Swift 2. I did leverage **closures**, **enumerations** and the new **error handling features** of the language to write a clean and easy to use API.

With **SwiftyStoreKit**, you no longer need to **explicitly** register an observer to the payment operation queue. You just call an asynchronous method for your IAP, and update your application state and UI on completion.

I borrowed ideas and code patterns from other popular open source projects. And I was happy with the results.

### 3. Write the best README you can

Your README is the **landing page** of your project. You should spend a lot of time on it.

It should **look** good! If you’re building a UI control, include an animated gif, screenshots, or even a link to a prototype. [Swift Messages](https://github.com/SwiftKickMobile/SwiftMessages) does this very well.

It should include badges so you can quickly glance at the status of the project. A lot of projects use [shields.io](http://shields.io/). So should you.

The README should highlight:

* What is the **feature set** and how to use the project by clearly **documenting the API**.
* **How to install** it. Note: Do support as many dependency management tools as possible, _not just [Cocoapods](https://cocoapods.org/)._
* **Supported platforms**. You guessed it, as many as you can.
* **Supported languages**, with links to appropriate branches or tags for different language versions.
* List of **known issues** (optional). This can serve as a summary of the current issues in the project.

Additionally, you can add a FAQ section, references to related projects and resources, a list of credits, and the [**license**](http://choosealicense.com/licenses/).

**Very important**: if your users open lots of issues asking for clarifications, your README is not good enough. Answer the questions and improve it accordingly.

**Include a sample demo.** This helps others using your project. It serves as a reference implementation, and shows how to integrate your code inside a real app.

### 4. Share in the right places

Some GitHub users maintain lists of popular open source projects by platform or language. I have submitted **Pull Requests** to include **SwiftyStoreKit** on [Awesome iOS](https://github.com/vsouza/awesome-ios) and [Awesome Swift](https://github.com/matteocrippa/awesome-swift).

Don’t limit yourself to GitHub:

* Find websites that aggregate open source projects and submit yours to them.
* Have your project featured in popular newsletters for your language or platform.
* Share on social media with relevant developers and accounts. Some good outlets are **Product Hunt**, **Hacker News**, **Twitter**, **Reddit**.

### 5. GitHub Trending = Lots of ⭐️⭐️⭐️⭐️⭐️

If you make it to the **GitHub Trending** list, your project can take off big time!

For me, it was a surprise. A colleague at work told me **SwiftyStoreKit** was on the Swift [weekly trending list](https://github.com/trending/swift?since=weekly) on GitHub. From there, I started receiving up to 50 stars a day!

How to make it into the **GitHub Trending** list? [Read this](https://blog.cwrichardkim.com/how-to-get-hundreds-of-stars-on-your-github-project-345b065e20a2#.ndsxn9v7g)).

**Note**: Right project + great visibility = a lot of interest. **Be prepared to keep up.**

### 6. Google Search

Google Search has been a big source of organic traffic:

![Image](https://cdn-media-1.freecodecamp.org/images/1*5UnDJgk2HK8kv0ufQQkWkQ.png)
_Main referring sites for SwiftyStoreKit_

In fact, searching for “Swift StoreKit” and “Swift In App Purchase” shows **SwiftyStoreKit** as the **second** and **fourth** result respectively:

![Image](https://cdn-media-1.freecodecamp.org/images/1*-uUd9yN2IK4hDYtQzPTfeg.png)
_Google Search for Swift StoreKit_

I have not done any keyword research to improve the SEO ranking of my project. It simply made to the top once it became popular.

Still, if you plan a good SEO strategy the results can be great!

### 7. Keep growing

Once your project is popular, people will ask a lot of questions and open pull requests.

At some point a [single contributor](https://github.com/phimage) ported **SwiftyStoreKit** to macOS and added receipt verification support. I had no experience in either area, and it felt great that someone was helping to make the project better!

Other valuable contributions followed after that, and I found myself wearing two hats: **main developer** and **maintainer**.

Being a good maintainer requires **good judgement**:

* Carefully evaluate feature requests. Aim to keep your API clean and avoid code bloat. This is especially true for **SwiftyStoreKit** as it is a _lightweight_ framework.
* For any pull requests that add useful functionality, don’t be afraid to request changes to keep the code clean and consistent.
* You can decline pull requests that are out of scope or if the existing code already covers them.
* Always be courteous to the contributors. If you reject their changes, politely explain why. Don’t be like [Linus Torvalds](http://www.theregister.co.uk/2016/07/11/linus_torvalds_in_sweary_rant_about_punctuation_in_kernel_comments/). ?

### Things I have learned

**SwiftyStoreKit** has been a great project, and pushed me into the maintainer role for the first time.

It forced me to increase my knowledge about in-app purchases, especially as other people made contributions.

This quote about stewardship feels appropriate here:

> In reality, the biggest challenge to a business open sourcing a project is the obligation of stewardship. This responsibility is mostly a matter of working with people and needs to be managed correctly — especially if a project gains enough popularity. Most projects don’t get large enough for their stewardship to become burdensome. — [Artsy Blog](https://www.objc.io/issues/22-scale/artsy/)

I have not always been able to answer questions on time. I hope to do better in the future, and improve my process in various ways:

* Add a CONTRIBUTING file outlining the recommended way of opening issues and pull requests, as popular open source projects do.
* Add a Code of Conduct.
* Add [code linting](https://github.com/realm/SwiftLint).
* Add **unit test** coverage, as I need **confidence** in making changes. Really, _I should have done this a long time ago_.

I’m right at the point where **SwiftyStoreKit** isn’t large enough to become burdensome to manage. I want this project to flourish, and welcome contributions from the community.

### Credits

Disclosure: A while ago I discovered this great story by [Richard Kim](https://blog.cwrichardkim.com/@cwRichardKim) on Medium:

> [How To Get Hundreds of Stars on Your Github Project](https://blog.cwrichardkim.com/how-to-get-hundreds-of-stars-on-your-github-project-345b065e20a2#.g8e2vl8hi)

This opened my eyes about what makes an open source project stand out. I have been following his advice since then. It really has paid off and I would like to thank him for the insight.

### Conclusion

Open sourcing can be a very rewarding experience, making you grow along with your projects.

I have helped teams in various companies for over 10 years, using a lot of open source software along the way.

Writing open source code is a great way of giving back to our great community, and I deeply enjoy the process.

#### Here’s to making the world better, one line of code at a time!

#### Update 2017–02–25: Read my follow up to this article about [Maintaining a Growing Open Source Project](https://medium.com/@biz84/maintaining-a-growing-open-source-project-1d385ca84c5#.legbfq8jl).

_About me: I’m a freelance iOS developer, juggling between contract work, open source, side projects and blogging._

_I’m [@biz84](https://twitter.com/biz84) on Twitter. You can also see my [GitHub](https://github.com/bizz84) page. Feedback, tweets, funny gifs, all welcome! My favourite? Lots of ???. Oh, and banana bread._

