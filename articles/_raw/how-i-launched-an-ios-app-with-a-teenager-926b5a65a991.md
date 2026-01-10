---
title: How I launched an iOS App with a teenager
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-01T23:58:44.000Z'
originalURL: https://freecodecamp.org/news/how-i-launched-an-ios-app-with-a-teenager-926b5a65a991
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0eG3vNBbMh7an5R3CY6Gmw.jpeg
tags:
- name: Apps
  slug: apps-tag
- name: education
  slug: education
- name: General Programming
  slug: programming
- name: teaching
  slug: teaching
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Sean Choi

  How to go from Scratch to an iPhone app in the App store

  As a follow up to two of my prior articles, (How to teach programming to teenagers
  and Beginner’s Guide to Raspberry Pi), I want to share my experiences in helping
  a teenager go fr...'
---

By Sean Choi

#### How to go from Scratch to an iPhone app in the App store

As a follow up to two of my prior articles, ([How to teach programming to teenagers](https://medium.freecodecamp.org/how-to-teach-programming-to-teenagers-2ecd43846f0d) and [Beginner’s Guide to Raspberry Pi](https://medium.freecodecamp.org/beginners-guide-to-raspberry-pi-6e55080fdaaf)), I want to share my experiences in helping a teenager go from coding in Scratch to building and deploying an iOS app.

As mentioned in [one of my prior articles](https://medium.freecodecamp.org/how-to-teach-programming-to-teenagers-2ecd43846f0d), I noticed that teenagers have a strong desire to do something that feels more real. So, the natural question that repetitively came up in many of my classes was _“Can we build an iPhone App?”._ I felt that the time was right for the students to build an app, and I asked them each to pitch an idea.

A week later, one of the students came back with an idea and it seemed really really interesting, so we decided to take some time outside of the regular class time and build it together. And we ended up with a cool app called [SwimGrader](https://itunes.apple.com/us/app/swimgrader/id1364739414?mt=8).

![Image](https://cdn-media-1.freecodecamp.org/images/SqaTFid-0S7n7JVHpIEGmz8spT13QTPUByVZ)
_Asian Games Swimming from [Wikipedia Commons](https://commons.wikimedia.org/wiki/File:Incheon_AsianGames_Swimming_19_(15178565298).jpg" rel="noopener" target="_blank" title=")_

#### How did SwimGrader come about?

My student is an avid swimmer and has always been curious how good his swimming is. Assessing your own swimming ability is not really obvious, and you often need some expert to tell you how good you are.

We all know that lowering lap time is the goal most athletes shoot for, so a lot of people attempt to do that. However, it is quite hard to know in detail what you must work on to achieve lower lap times. Of course, you can just try to kick faster and practice more to gain more swimming muscles, but that usually is not the best way to improve your swimming.

Coming from this, my student thought that people needed something that could pinpoint an area of swimming they should work on next. So, his brilliant idea was to build an app that could assess various aspects of your swimming and tell you which area you should work to improve.

Knowing from experience how hard it is to improve my swimming, I was **really** impressed by his idea. It was nothing that I had heard of before and it had a specific use case that could potentially benefit a lot of people. However, since my student had never built an iPhone app before, we decided to work on it together from scratch.

#### Getting started

Not being a competitive swimmer myself and also thinking that it would be a good thought exercise, I asked my student to come up with the design of the app and the metrics we could use to grade the swimmer in the app.

This process ended up to be a really good learning experience. Not only did this exercise helped the student iron out the details of the project, but it also kept my and my student’s expectations in line. As mentioned in my articles about teaching teenagers, teenagers have high expectations about doing anything with programming. So, after talking through every detail from which data to collect, which pages to create, how each page transition works and which metrics to show, both of us were to clearly set our goals and our expectations.

And knowing the exact end-product we were planning to make helped the student stay constantly engaged.

Digressing a little bit from the main topic, we often learn things that we don’t know when we will ever apply in our lives. This can make us feel like we are walking through a long dark tunnel with no light at the end.

This is especially true when you are younger, as you are most likely being told to learn certain things. I believe that this causes many students to not get excited about what they learn. I learned that setting the right expectations by showing the end of the journey of a learning exercise really helps motivate students and increases the efficiency of the learning exercise itself.

So, back to the design and the metrics of the app that the student suggested: my student first suggested that the app, in general, should not add any overhead for the swimmer. He wanted to build an app that would be able to collect statistics without hampering the swimmer’s performance.

The student already had a measuring device in mind to serve this exact purpose, which I will share in the next section. After some discussion to come up with a minimal viable product, we decided that we should focus on collecting two specific metrics: **head bops** and **turn speed**.

Since head bops are a mostly extraneous movement that can reduce the efficiency of swimming, if we can simply count the number of head bops within some time interval, we thought that we could suggest a reduction in extraneous head movements.

We also agreed that fast turns are necessary for reducing lap times. So, if we could measure the time it takes the swimmer to make a turn at the end of the lane, we could grade the swimmer based on time.

Given this design and the idea, we only needed to start implementing it with the right sensor.

#### So, which hardware made SwimGrader possible?

![Image](https://cdn-media-1.freecodecamp.org/images/9aLWiVhSZZeCfqgwKTSqVAaddclmgStXu9tb)
_mbientlab’s sensor research kit_

Although the latest [iPhones](https://amzn.to/2RZbPH1) are waterproof, swimmers probably don’t want to risk taking their [super expensive iPhones](https://amzn.to/2RZbPH1) into the pool. So, my student suggested that we use a [sensor](https://amzn.to/2CpAnUi) from [mbientlab](https://mbientlab.com/product/mountable-sensor-research-kit/) and enclose it in a waterproof case.

This sensor allows you to collect various data from the environment and from your movements, as it houses an accelerometer, a gyroscope, a barometer, a thermometer and so on. Also, they have some [sample code](https://github.com/mbientlab/MetaWear-SDK-iOS-macOS-tvOS) that you can use to bootstrap your application so you can immediately collect the data of interest.

So, our idea was to put the sensor inside his swimming cap. He felt that this would minimally impact the swimmers’ ability to swim, which I agreed with. We immediately purchased two of these sensors and started building our app. I will not go over the details of building a simple multi-page iOS app using Swift, because they have covered in thousands of other articles ([here](https://hackernoon.com/the-ultimate-list-of-resources-to-mastering-swift-and-ios-development-2018-edition-3bd2a87ff400) is a good medium article that presents many of them).

![Image](https://cdn-media-1.freecodecamp.org/images/ktN8sHcvZNgzVcV4mval6VErSN3sHmepTzuS)
_SwimGrader App Window_

#### Introducing SwimGrader

So, after hours of programming and going through Apple to get our app approved for the App Store, we were finally able to launch [SwimGrader](https://appadvice.com/app/swimgrader/1364739414). It was really surprising to see this, because I only helped with the initial setup of the project, which consisted of setting up a single page app Swift project and helping with adding buttons and text fields, and simple hardware integration to retrieve data from the sensor.

To give a sense of how easy the hardware integration was, here is a snippet of code to make the LED on the sensor flash green. Retrieving data was just as simple, as can be seen by the example below.

```
import MetaWearimport MetaWearCpp
```

```
MetaWearScanner.shared.startScan(allowDuplicates: true) { (dev) in    // We found a MetaWear board, see if it is close by    if dev.rssi.intValue > -50 {        // We found a MetaWear board!        MetaWearScanner.shared.stopScan()        // Connect to the board we found        dev.connectAndSetup().continueWith { t in            if let error = t.error {                // Sorry we couldn't connect                print(error)            } else {                // We are connected! Flash its LED!                var pattern = MblMwLedPattern()                mbl_mw_led_load_preset_pattern(                    &pattern, MBL_MW_LED_PRESET_PULSE)                mbl_mw_led_stop_and_clear(device.board)                mbl_mw_led_write_pattern(                    device.board, &pattern, MBL_MW_LED_COLOR_GREEN)                mbl_mw_led_play(device.board)            }        }    }}
```

Given only a limited about of help, my student went far beyond my expectations to build a grading algorithm and a graphical interface. He retrieved the X, Y, Z data from the sensor and gave a grade on how much the head moved in each direction. He searched online for a graphing library on iOS and displayed what his sensor reported. And, after finishing his app, he went ahead and tested his app in the pool!

It is an effort by a middle school student, so it’s not going to look fancy like Clash of Clans. However, I think it is really impressive, coming from a young student who has never built an iPhone app before! After finishing this, the student asked me,

> Can we build an Apple Watch App for this?

I told him that he could definitely build an Apple Watch version of the app in the future, but that he could probably build it without my help :).

#### Final Thoughts

As grown-ups, I think it is really hard to keep our ideas fresh, wild and up-to-date. So, I think it’s really educational to hear what these young students have to say and to support what they want to do in all the ways we can.

Not only do these opportunities open the gate to building new and exciting products, but supporting students to pitch and build their own ideas gives them the best educational experiences. Seeing my student asking people to download his app makes me smile. I am hoping that I can maybe build a cool app someday and showcase it to my friends. Although, my student just beat me to that :)

On a side note, I learned that building a cool iOS app is easier than ever. There are so many articles helping you build apps for every possible purpose: games, single view apps, social network apps and many more. Also, there is more hardware than ever that you can easily hook up to your phone and extend the capabilities of your phone.

I hope I can soon share experiences of building my own app. I am just worried if my students will find my app cool…

Thank you for reading this article! I hope I can convince you to work with your students or your children and start building a simple app! I am also open to hearing about your cool app ideas.

