---
title: Today I launched my first mobile app. Here’s what I learned
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-28T14:22:33.000Z'
originalURL: https://freecodecamp.org/news/today-i-launched-my-first-mobile-app-heres-what-i-learned-6fc25c14eee6
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yUKmN6_dAlYalYjlsu57_w.png
tags:
- name: Cryptocurrency
  slug: cryptocurrency
- name: Design
  slug: design
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: startup
  slug: startup
seo_title: null
seo_desc: 'By Harshita Arora

  I’ve been writing a fair bit on Medium recently, sharing valuable design and development
  knowledge I gained from working on my first app, Crypto Price Tracker that I just
  launched today, on 28th Jan.

  I wanted to share my story of wo...'
---

By Harshita Arora

I’ve been writing a fair bit on Medium recently, sharing valuable design and development knowledge I gained from working on my first app, [Crypto Price Tracker](https://itunes.apple.com/us/app/crypto-price-tracker/id1333696099?ls=1&mt=8) that I just launched today, on 28th Jan.

I wanted to share my story of working on this app from the day I started until today. I hope this post helps and inspires other young programmers (or really anyone who’s interested in making tech products!) to acquire valuable technical skills, identify market needs, build great products with their skills that solve those market needs.

A bit of background on me: I’m a 16-years-old homeschooler. I’ve been learning digital design and programming since I was 13. I was the youngest intern at Salesforce in Bangalore in winter 2016.

I attended MIT Launch summer program in 2017 summer where my team and I launched [Universeaty](http://universeatyapp.com/). That was the first time I tried my hands at iOS apps and loved how much faster it was to build tangible products and see results of my work when building mobile apps. Bringing my ideas to software was much easier and more fun!

I started learning Swift and iOS app development from online courses on [Treehouse](https://teamtreehouse.com/tracks/beginner-ios-development), [Udemy,](https://www.udemy.com/ios-11-app-development-bootcamp/) watched videos on YouTube and practiced building basic apps. That laid out my programming foundations. I started building more serious and complex apps after a few weeks of learning and practice.

Around 20th November, 2017 I decided that I wanted to work on a cryptocurrency price tracker, alerts, and portfolio management app. I’ve shared a bit of the story about my motivation [here](https://blog.usejournal.com/a-sneak-peek-at-a-beautiful-new-cryptocurrency-price-tracking-portfolio-and-alerts-app-bd16c3985134). I recently realised that sharing my story and some of the lessons I learned along my journey is indeed helpful to others!

### Getting Started

It was hard to get started: uncertainty, unknown unknowns, things to think about, and decisions to make. No clue what to start with and where. But I knew my first step was conducting some market research to know exactly what my target audience wanted — the features, the design, and just about everything that I’d build in the app.

I posted on Reddit, Facebook groups, Quora, and asked a few friends who were invested and interested in cryptos. I got some solid feedback on the idea and was much more educated about the needs of my target users.

The next step was to design the app. I started with drawing the user-flow diagrams and wireframes. I then moved on to using design software to create mock-ups and a prototype. I’ve written a different [story](https://medium.freecodecamp.org/designing-beautiful-mobile-apps-from-scratch-1a3441ebd604) about designing mobile apps from scratch, and I’ve shared pictures of every design stage of Crypto Price Tracker app.

And the end result of this process was this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*yUKmN6_dAlYalYjlsu57_w.png)
_A delightful design :)_

### Developing Crypto Price Tracker

I was pretty afraid of reaching this stage, because I was (and still am) a programming beginner. I didn’t know a lot of Swift and had no clue how I’d set up the server for notifications, among many other technical hurdles. I had so much stuff to do for the app with little technical skills. But I was confident I could figure out things and learn along the way as I build each feature. And, in hindsight, I can say I did :)

I started out with importing all the designs in Xcode and setting a raw build for every screen. I divided my coding work based on features I’d need in the app. Quite a few times, I had to scrap things off my spec (and edit designs) because they seemed time consuming to develop (especially if it seemed that they’d offer little functionality).

I wrote the networking code to display data from the APIs I was using and built the main interface of my app. I then moved on to the “Wishlist” feature of the app. Now, to save data locally in a user’s phone, you need to create Core Data models — something I had never worked with before. And more technical gaps and challenges came up.

But I kept on learning. When I needed something, I’d Google it. Usually, there were helpful answers, code snippets, or video tutorials for almost everything. Whenever I got stuck, I would ask on StackOverflow or email my mentors for help. Slowly, I started becoming much more comfortable jumping into unknown things.

At the end of the three weeks that I spent coding the app, I improved a lot as a programmer. I learnt concepts and got to actually practice by building a real app. I got to work with a number of interesting iOS technologies, libraries, and frameworks.

I still need to improve a lot as a developer. My app sometimes loads slow. It’s not the most optimised or the fastest app out there. But I’m still pretty glad I was able to build something useful and valuable.

The next step I had planned was that I’d localize my app in 10 languages. I thought it was easy since my app isn’t text-heavy. Boy, I was wrong! Localization is a very time consuming process for apps. I’m writing a separate story to explain how to localize technically.

At the end of 8 weeks (from the day I started market research), I had fully designed and developed an app that showed real-time prices of over 1000+ cryptocurrencies from 18 exchanges in 32 fiat currencies. There were price graphs (showing historical prices from 1 day, 1 week, 1 month, 3 months, and 1 year), portfolio management, time-based and threshold-based alerts. It was localized in 10 languages. I also optimised my app for iPhone X.

Once my build was ready, the next step was to invite users to test and give feedback on the app.

### Testing and Submitting the App

I was quite proud of my app and was super excited to put it out there on TestFlight and invite all of my friends and users to test it! After a long wait of two days, the beta app review was finally approved. I invited my friends to test it and they loved the app. All of them shared feedback, ideas for features to have in future updates, and much more. The app had zero crashes!

The v1.0 build was all ready for submission. My 100 screenshots (5 screenshots for iPhone 5.5 inch and 5 for iPhone 5.8 inch for each language) were ready, my metadata was localized too, and my video preview was done.

There were some unexpected challenges in uploading the video preview because the fps (frames per second) was too high. By this point I had grown to embrace unexpected challenges and was able to handle them effectively. I was able to finish everything and submit the app for review on time.

Two days later, at 4AM, I got the rejection email.

This made me extremely anxious. So many thoughts were rushing through my head before I read the reasons for rejection. Apple rejected the app because the design didn’t look good when viewed on iPad. I had no clue that iPhone-only apps had to be compatible with iPads as well. In the next few hours, I read some guides and fixed all the constraints and Auto Layout issues, tested the app on iPad simulator and it worked. I submitted the build for review again.

One day later, I finally got the approval! It was a relief, and now I could focus back on the product. I had gotten a ton of feedback and bugs reported from testers. I made those small bug fixes and some translations edits, and uploaded the final build. It got approved in just 12 hours! My app was now a whole lot better and I’m glad so many people tested it and reported bugs that would have otherwise gone in the app reviews by angry customers.

In the days leading up to launch, I put together this story from the notes I made and my daily journal so I could share the lessons with everyone.

### Some Lessons I Learned

1. Localization is a great idea. Until now, I was regretting my decision of localizing my app in 10 languages. I’d written some [Quora answers](https://www.quora.com/How-do-you-localize-your-metadata-in-the-iOS-and-Mac-App-Store/answer/Harshita-Arora-16?share=9cb57341&srid=ud5cQ) on how it was the most time-consuming thing I did for my app and I’d not advise any indie developer without the budget to outsource to localize. But now my opinion has changed. Localizing your app in 10–12 languages using Google Translate and having friends proofread it is a great way to reach a larger audience for your app. Apple also loves localized apps more. You can’t always get everything right and every possible string localized. But you can get 80% of the results (i.e., text translated) with the 20% of the work.
2. People are much more willing to help you than you think. I am very grateful to have a number of friends and mentors who helped me a lot in this journey. But I was simply astonished how so many strangers responded to me when I reached out to them and helped me. Very early on in my journey, when I just had a little prototype of the main interface of my app, I reached out to [Carla White](http://carla.is/) after I had read her amazing book. She mentored me and helped me with her advice for the app. As I was localizing my app, I needed proofreaders for each language to make sure the translations (done using Google Translate) are good and context specific. [Pascal](https://twitter.com/DJCalled) commented on my story on Medium offering his help with German translations. I reached out to him and on a really short notice, he really did edit my German translations! And many more complete strangers offered their help.   
One important key takeaway from this would be: People are willing to help you. Reach out to them, be sincere, and they will help you in any way they can! :D
3. User feedback early on is super critical. Not only do the kind words from your fans or believers motivate you, but a lot of your early users will give you ideas for features, for design improvements, and much more valuable feedback. One of the mistakes I made was testing very late. I uploaded my build for TestFlight testing only ~1 week before planned launch when the app was pretty much ready and I couldn’t make major changes. If I had asked my users to start testing weeks ago when I just had the main interface, I’d have gotten lots of feedback and would have improved upon it. And iterated that for every major feature, my app would have been a whole lot better. Quite a few testers have mentioned things that could have been fixed in 2–3 days if I had sent out the build for testing earlier. So my advice to everyone would be: Get your app in the hands of your users and have them test it asap and get feedback!

### Some Helpful Tools I Used

1. [AppLaunchPad](https://theapplaunchpad.com/) for creating multiple sets of screenshots (for many localizations) faster.
2. [Cocoapods](https://cocoapods.org/). [SwiftyJSON](https://cocoapods.org/pods/SwiftyJSON) and [Alamofire](https://cocoapods.org/?q=alamofire) for writing better networking code, [Charts](https://cocoapods.org/pods/Charts) for creating price graphs. There’s a cocoapod for almost everything!
3. [Firebase](https://firebase.google.com/) for the push notifications server and for the caching server to store prices every 5 mins to update the price graphs.
4. Two APIs for prices: [cryptowatch](https://cryptowat.ch/docs/api) and [CoinCap](https://github.com/CoinCapDev/CoinCap.io). This [API](http://fixer.io/) for currency rates for conversion.

It feels great to be able to share the lessons I learned and my journey with a large audience. I hope this serves as an inspiration to other people to try out learning programming and building apps or really anything they’re interested in. I’m personally going to start out with learning ML and data science after my app — so don’t be afraid of experimenting with different fields! Try out something difficult and something that makes you uncomfortable. The things hardest to do are usually the most interesting and rewarding in the end. :)

If you liked reading this and have feedback or any thoughts to share, don’t hesitate to email me at harshita@harshitaapps.com. And if you like my app, you can download it from the App Store [here](https://itunes.apple.com/us/app/crypto-price-tracker/id1333696099?ls=1&mt=8). :)

