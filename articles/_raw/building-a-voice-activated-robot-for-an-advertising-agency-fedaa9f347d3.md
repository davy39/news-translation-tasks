---
title: Insights I gained from building a voice-activated robot
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-05T17:40:58.000Z'
originalURL: https://freecodecamp.org/news/building-a-voice-activated-robot-for-an-advertising-agency-fedaa9f347d3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lbIDINee-izLUwkgIb581g.gif
tags: []
seo_title: null
seo_desc: 'By Mithi


  Insights I gained from building a voice-activated robot


  For almost a year, I worked at an advertising agency as a creative technologist.
  Based on the insight that innovation drives new businesses and that technology can
  be creatively appli...'
---

By Mithi

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ao2FdjrlyNOlixjPtXD7Cg.jpeg)

# Insights I gained from building a voice-activated robot

![Image](https://cdn-media-1.freecodecamp.org/images/1*lbIDINee-izLUwkgIb581g.gif)

For almost a year, I worked at an advertising agency as a [creative technologist](http://digit.gitlab.io/digit-x/). Based on the insight that innovation drives new businesses and that technology can be creatively applied to brand campaigns, there are a few interesting things I do at my job. I introduce new technologies, do feasibility checks of tech ideas by non-tech creatives, and [prototype stuff](https://docs.google.com/presentation/d/18nTykqw-Evj0o0kAuIuKrMsknV8-LQz7Obmxvazd1wQ/edit?usp=sharing), among other things.

Perhaps one of the most exciting things I did at my job was working with robots! I oversaw the creation of and programmed a 45-inch tall robot for a little more than two months.

### How we built Robbie

Meet Robbie — also known as [HelloBot](http://digit.gitlab.io/digit-x-robot/) — an experiment in how humans and technology interact by getting people to connect with a robot the same way people connect with other people. The idea behind Robbie is that technology, such as a robot, can reinforce your brand with each delightful interaction.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EwOqyh2QmjSAI-ZsD8fgLg.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*CfIj9YaFMg4zsJ1o_4OzMQ.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*ASspWUHMXcbvs_25y15IoQ.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*IhER4KvG8sF8CpByaBNITw.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*O1dMfn33Oj88-3gJ3TKm7w.jpeg)
_Some insights I got from the creative process of building the “minimum-viable-product” robot version of Robbie._

It’s easier now more than ever to build a sophisticated robot with off-the-shelf parts.

This is all thanks to the open-source hardware (OSHW) community. Building a robot is possible because we are standing on the generous shoulders of giants.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ytlKHwxvDr0QxF57PGJGmQ.png)

All of the electronics used to build Robbie can be bought from [DFRobot](http://dfrobot.com), [Adafruit](http://adafruit.com), and [Hobby King](http://hobbyking.com). All of them are open-source — the schematics, bill of materials, and PCB board design are free for anyone to download, replicate, or modify.

Each component is not a black box where you have to rely on a small customer support team to troubleshoot your issues. When something goes wrong, you have a whole community to help you.

Also, because plenty of information is freely given to you, you gain a deeper understanding of how things work.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Y8TWQZcSb8afA6YVwZOn3g.png)

The brain of our robot is a [Raspberry Pi 3](http://raspberrypi.org), a credit-card sized WiFi-enabled computer. It is connected to a variety of peripherals so the robot can get input and output from the outside world.

Some of the inputs are: a microphone so that the robot can hear your words, an 8-megapixel camera so that the robot can see you, and a passive infrared (PIR) sensor which activates when the “average radiation level changes.” This is useful in detecting if human beings move in or out of the robot’s territory.

Some of the outputs are the 7-inch display where the robot shows its expressions, and audio speakers so you can hear what it’s saying. The Raspberry Pi 3 is connected to WiFi and uses [Google’s speech recognition library](https://cloud.google.com/speech/) . It uses an open computer vision ([OpenCV](http://opencv.org/)) library to recognize faces.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fs7Rac0WtXGOVXOc8QTKBw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Uby_FKtAS17bEQqoaCgcAA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Go_98roPwBS-v29WreJonQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*j9ye4Fc-7IHgN1o3VvJrFw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*XPN79SUj4KgneTd__oVx7Q.png)

The Raspberry Pi 3 communicates with an [Arduino Mega](http://arduino.cc) microcontroller to delegate low level tasks that the Pi is not good at. The Arduino Mega controls two motor drivers (it has four wheels that you can control independently) so that the robot can move left, right, forward and backward.

It also has two servo motors (special motors that can be steered by angle because of built-in feedback circuitry) to move its arms.

There are also lower level peripherals connected to the Arduino such as colorful RGB-addressable chainable LEDs “[Neopixels](https://www.adafruit.com/category/168)” to indicate status, and three infrared distance sensors to avoid obstacles.

![Image](https://cdn-media-1.freecodecamp.org/images/1*eRBynzsjCT4rBkWus6EQDQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*5AhcgK5hhx6I7Q8cnFXVFw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*d42GY-71f49-BO0qO2az3A.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*UBpqeq23_NSHpTsq6Nr2Wg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*C54Waq3zARr3bQjZJdD5pw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*kqkZnCZ03zp0rl7nKpP2VA.png)

The whole robot (including the motors) is powered by 14.8v 4500 mAh lithium polymer batteries. DC-DC converters regulate the power to bring it down to a lower voltage required to power the Raspberry Pi and Arduino safely.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IOu2YTtIzPYhjKJyCOeOUQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*SlxuVaf8IMv3PfJNP52p_Q.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*meNEUTZBF699GTbpRIuZZw.png)

We wouldn’t have been able to design, much less understand, any of this if it weren’t for the generous tutorials made by the open-source hardware community — particularly by [Adafruit Industries](http://adafruit.com), pioneered by [Limor “Lady Ada” Fried](https://en.wikipedia.org/wiki/Limor_Fried).

Here are some of the things I learned throughout this process.

### Designing “clean code” is crucial

![Image](https://cdn-media-1.freecodecamp.org/images/1*7aqCLMcrRsC1z3XL3uqMgg.jpeg)

Trying to design “clean” code is very important when you’re trying to build a robot that you’ll love not only to interact with but also build upon.

I’ve learned to be thoughtful when writing code for this robot, as inspired by code craftsmanship books by [Robert Martin](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882) and [Sandi Metz](https://www.sandimetz.com/). I’m not a veteran in writing well-crafted code, but I try my best.

When you do code maintenance in a robot, you can really “love” or “hate” a person that you do not even know just because of the code they have written.

Messy code almost always goes hand in hand with lower productivity, lower motivation, and a higher number of bugs. Countless hours and significant resources are lost because of poorly written code, but it doesn’t have to be that way.

Clean code is something that’s been on my mind for a while. A year ago, I spoke at [Python Conference Philippines](https://medium.com/nanica-talks/nanica-io-talk-a-raspberry-pi-hexy-transcript-d39257ac7cdc#.kq3lt4p7j) about how I made a robot hexapod dance in the effort to practice writing clean code. I spoke about my guiding principles for thoughtfully written code.

Even earlier, I wrote about [things I think about](https://medium.com/@mithi/review-sandi-metz-s-poodr-ch-1-4-wip-d4daac417665) when I decide to write my own classes. It’s part of my effort to apply an object-oriented design philosophy to make my code clean.

I still have these principles and thoughts at the back of my mind whenever I write code in general, and in particular when I wrote [the code for Robbie](https://github.com/mithi/hellobot-raspberry).

![Image](https://cdn-media-1.freecodecamp.org/images/1*UYF78LVNFkCJV4i9W_oavg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*rCZipTusi6cIbhpGUUYyrQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*n6jAs6mFkdoz-a8RPYlqTA.png)

The code residing in the [Arduino](http://github.com/mithi/hellobot-arduino) section is written in a simplified version of C++ designed for embedded programming. It has two obvious classes, `Motors` and `DistanceSensors`.

The `Motors` class is responsible for driving the wheels to make the robot turn left, write, move forward or back.

The `DistanceSensors` class is responsible for getting the distance and checking if there are obstacles around.

There are other classes that I’ve used that were made by other people, such as `Serial` and `Neopixel`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qfWOpD6_uaTRLjZE5YWn4w.png)

The code residing in the [Raspberry Pi](http://github.com/mithi/hellobot) section is written in Python. Some of the classes I’ve written for it are `Listener`, `Responder`, `Directive`, `Relayer`, and `FaceFinder`.

A `Listener` instance is needed to get the phrases (in string format) from the data from the microphone, as interpreted by GoogleSpeech.

The `Responder` plays videos or shows pictures on the screen.

The `Directive` processes the phrase to get the word after a **keyword** that is used to issue commands for the robot to execute.

The `Relayer` communicates with the Arduino.

The `FaceFinder` is responsible for detecting faces.

For cleaner code, classes should be responsible for only one thing and nothing more. Classes are created to make things simpler, not complicate things. You know a class is simple when you can describe what it does in one sentence like I just did.

### Learning through experience is the way to go

You need continuous iterations and user feedback to achieve a good user experience for your product.

Robbie in its current state is only a “minimum viable product”. There are still many things that can be done to improve the reliability, user experience, and overall design of Robbie.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7GRlsGxGrXvTbaHS-YXGVg.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*fFaQQ74ezmW2ttOiE64law.jpeg)

At the start, we designed Robbie to have various modes (**autonomous** mode, **camera** mode, **remote control** mode, **conversation** mode), that can be toggled by pushing buttons.

But when people started interacting with it, we realized that Robbie was going to be a voice-activated robot 90% of the time. Whenever people encounter Robbie, their instinct is to move towards the robot and talk to it.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XzoRTl4gL7B2lJZgRAcvzQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*UZ6ERqQ2UYzbicsO58xY2g.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*_XoTS1r9mOj3bpPux-u-Sw.png)

We realized how important it was for Robbie to have a better microphone and better audio speakers, as opposed to adding more sensors for a more reliable obstacle avoidance.

![Image](https://cdn-media-1.freecodecamp.org/images/1*9uhWYeoYf-OdqeVvCfgrYA.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*K_Iif14NoqYip9CN7QXCFw.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*vEHZ4Sm_GLDkkRyagsDUgw.jpeg)

We decided we needed to use a better more powerful omni directional mic. Currently, you have to speak inches above the mic in order to be understood by the robot. So now, the aim is for the robot to understand the commands even if the person is speaking a meter away.

People get frustrated when Robbie misunderstands. This is very dependent on the sound conditions of the room.

A conversation goes both ways. Improving the sound system is also one of the main priorities. Depending on the atmosphere of the room, even when Robbie understands the person, the interaction isn’t fun when the person doesn’t understand Robbie.

We also destroyed batteries because we accidentally left the robot turned on without the battery checker plugged in. The batteries got drained beyond the threshold. This was a very expensive learning experience for us.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rW1NRyRizYpMDe4a4zAyCw.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*ABIUhvk1tQ7ZnngFWOeWrg.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*nHtN7tWVVIsYpDrP51KiNQ.jpeg)

The arms of the robot are also a major source of pain. The arms were not mechanically designed properly. They are very fragile, so fragile that mere transportation of the robot would wear them down significantly. Sometimes an arm would fall off and it would be a pain to put it back on.

We have to design the arm not only to be sturdier but more modular so that it would be easy to put back on if it falls off.

![Image](https://cdn-media-1.freecodecamp.org/images/1*W8r5hxh0w1NFzbf9ZkrjiA.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*YmnvLYOmCgq8Ydf4g1GKlg.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*4qO0oWAYqXCrrg-L0B2Wqw.jpeg)

Speaking of modularity and pain, troubleshooting the electronics of the robot was the most painful process of all. Accessing the electronics was no easy task, because there’s no “easy-access door” and the boards were just drilled all over the place.

You have to dismantle the head of the 20 kg heavy robot just to get a multimeter inside. It was horrible. I cannot stress this enough. The next time I build a robot, designing for modularity and ease of troubleshooting would be at the top of my priority list. If there is “clean code” there is also “clean electronic integration and assembly”.

Poorly integrated electronics can function. But if things are not thoughtfully assembled or organized, when something goes wrong, nobody will want to fix your robot.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VLwI5e6qmptXA8gWGHsLSQ.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*jQBMRB3qKo8Y8IztKD8b8g.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*GlbFsRr8XaA3iMrT_s8YaA.jpeg)

### Wrapping up

There you have it, my three main insights.

First, it’s easier more than ever to build a sophisticated robot with off-the-shelf parts. This is all thanks to the open-source hardware (OSHW) community. Building a robot is possible because we are standing on the generous shoulders of giants.

Second, ideas in designing “clean” code are crucial to building a robot you’ll love and want to work on.

Last but not least, you need to learn through experience, continuous iterations, and user feedback to achieve a good user experience for your products.

I thank my previous employer for giving me the opportunity to grow and work on exciting projects. Being a creative technologist at an advertising agency has truly been a great learning experience.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sVa4kAS2dueSvy-OzbvtGA.jpeg)

Credits

* Tel Castillo — Poster Designs
* Apol Sta Maria — Creative Direction, Robot Design and Animation
* A lot of other people including but not limited to Dom De Leon, JR Ignacio, Axel Raymundo, Merlee Jayme, Alex Syfu, Owel Alvero, Jopy, Cyri, Cathy, Bonat…

![Image](https://cdn-media-1.freecodecamp.org/images/1*Oc4X-6kCJgUMCh63AeP9_g.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*yOUdk_ouqeS7agPeMJlz2Q.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*PtnqkSJsedi_Ye62rxUWdA.jpeg)

