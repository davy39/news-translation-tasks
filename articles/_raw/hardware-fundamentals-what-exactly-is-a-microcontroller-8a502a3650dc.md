---
title: 'Hardware Fundamentals: what exactly is a microcontroller?'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-04-24T13:18:27.000Z'
originalURL: https://freecodecamp.org/news/hardware-fundamentals-what-exactly-is-a-microcontroller-8a502a3650dc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*WKKNCMKqg6yEkowj28CHng.jpeg
tags:
- name: arduino
  slug: arduino
- name: hardware
  slug: hardware
- name: Internet of Things
  slug: internet-of-things
- name: Makers
  slug: makers
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Taron Foxworth

  At the fundamental level, a microcontroller is a just tiny computer.

  Being a “tiny computer” doesn’t really tell us much, though. So let’s go deeper.
  Many people associate microcontrollers with Arduino. But it’s important to point
  o...'
---

By Taron Foxworth

At the fundamental level, a microcontroller is a just tiny computer.

Being a “tiny computer” doesn’t really tell us much, though. So let’s go deeper. Many people associate microcontrollers with Arduino. But it’s important to point out that **Arduino is not a microcontroller**. Arduino is a complete platform which spans across software and hardware.

Arduino makes devices like the [Arduino Uno](https://www.arduino.cc/en/Main/arduinoBoardUno):

![Image](https://cdn-media-1.freecodecamp.org/images/1*GT8uC4hwFJfFb818C5g7LA.jpeg)
_Arduino Uno_

The Arduino Uno is not a microcontroller, either. It’s a breakout board based on the [Atmel ATmega328P microcontroller](http://www.microchip.com/wwwproducts/en/ATmega328P).

Here is what the Atmel microcontroller looks like:

![Image](https://cdn-media-1.freecodecamp.org/images/1*dGZ5XWLj4osrGlUf79mW1w.png)

If you were to have just the Atmel microcontroller in hand, as a beginner, it wouldn’t be very useful. This is where the breakout board comes in.

The breakout board “breaks out” the pins on the microcontroller into a larger device (like the Arduino Uno). This larger device makes the microcontroller easier to use.

For the Arduino Uno, the breakout board gives you the ability to insert a USB cord, give it power, program the device, and more.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jmPJwZqvF1QqNR0Xr_rmCw.jpeg)
_[Image credit](https://www.hackster.io/hmkim/remote-controlled-8x8-led-matrix-e2b79a?ref=part&amp;ref_id=8233&amp;offset=18" rel="noopener" target="_blank" title=")_

Without the breakout board, for a beginner, this would be a daunting task. This problem is the very reason that Arduino exists — to make it super easy for you to learn about hardware.

### Ah, So it’s like the Raspberry Pi?

Well, not entirely. Both the Arduino and the Raspberry Pi are still computers by definition. But the Raspberry Pi is considered a [single-board computer](http://maxembedded.com/2013/07/introduction-to-single-board-computing/). A single-board computer is [a full computer built on a single circuit board](https://en.wikipedia.org/wiki/Single-board_computer).

![Image](https://cdn-media-1.freecodecamp.org/images/1*iK9lfwT4cpJsY4lWQ2ul0Q.jpeg)
_A Raspberry Pi_

Your laptop is also technically a single-board computer — just a powerful one. The Raspberry Pi is a simple version of the same hardware in your laptop. Just as your laptop runs an operating system (Windows, Mac, or Linux), the Raspberry Pi runs a Linux operating system.

Now, back to Microcontrollers. Microcontrollers can’t run an operating system. Microcontrollers also don’t have the same amount of computing power or resources as most single-board computers.

A microcontroller will run just one program repeatedly — not a full operating system. We can see this in Arduino programs because they only need two functions: `Setup` and `loop`. `Setup` will run once and `loop` will run indefinitely.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2zfsMFC_vB9OMA81Hl5ITA.png)
_Setup and Loop_

### So, what’s a microcontroller?

A microcontroller is a small computer with low-memory and programmable input/output peripherals.

#### Inputs/Outputs

As you probably know, everything with a computer eventually starts with binary (0 or 1).

![Image](https://cdn-media-1.freecodecamp.org/images/1*GFnxrpbOLyCUBuhnwxIHNA.png)

An input means that the microcontroller will read binary. An example input would be a sensor.

An output means that the microcontroller will send binary. An example output would be to control a motor or LED.

### Why do we need microcontrollers?

Well, these were “computers” before we arrived at the idea of the computers you know today. Microcontrollers stuck around because some computing tasks are incredibly trivial and require simple logic. For example, flipping a switch or controlling small components — like a LED light — don’t require the same resources we need for day-to-day tasks like sending an email.

We use them today because their low-powered and low memory makes them low-cost. Microcontrollers are part of the reason the [Internet of Things](https://en.wikipedia.org/wiki/Internet_of_things) is possible and successful today.

### How do I get one?

Which microcontroller you’ll want to get depends on which problem you want to solve. If you are doing something simple — turning things on and off, or reading a sensor — pretty much any microcontroller will do.

If you want to play games or have more complex ideas, you’ll need more compute power, so you’ll need to move up to single-board computers, like the Raspberry Pi.

[Adafruit](https://www.adafruit.com/) and [Sparkfun](https://www.sparkfun.com/) both have TONS of kits and hardware that are all amazing. You can also make use of their tutorials.

[Losant](https://losant.com) also has some cool [kits](https://docs.losant.com/getting-started/losant-iot-dev-kits/builder-kit/) available. You could build your own [door sensor](https://docs.losant.com/getting-started/losant-iot-dev-kits/door-sensor-kit/) — to be notified when a door is left open for too long.

If you don’t have a specific problem you want to solve, just grab some hardware and play around with it.

Here are some things you can buy to get started:

#### 1. A board called the [NodeMCU](http://amzn.to/2oyalUf).

![Image](https://cdn-media-1.freecodecamp.org/images/1*lVu30df4maR8KAoG1vKDlg.jpeg)
_Node MCU_

The [NodeMCU](http://amzn.to/2p3YDEu) is a board based on the ESP8266 microcontroller. This board is special because it’s cheap and WiFi enabled. It will only run you about $8.79 on Amazon and is even less on Ebay.

Not all microcontrollers are WiFi-enabled. The fact that this one is opens the door to a number of projects you can build with this device. For example, you can collect data and send it to the cloud ☁️.

#### 2. You’ll need some [Sensors](http://amzn.to/2ocLN7O)

![Image](https://cdn-media-1.freecodecamp.org/images/1*tJrDBAK3Gi1gd3EucYqsnw.jpeg)
_Bread Board_

You can’t have hardware without sensors. Sensors give you the ability to detect the environment and the world around you. They’re also a great tool for learning.

#### 3. You’ll need a [Breadboard](http://amzn.to/2oul4zW) & [Jumper Wires](http://amzn.to/2p0stYM):

![Image](https://cdn-media-1.freecodecamp.org/images/1*hzlbvjGieO28VE7VKbFFZw.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*-Ts_mndGd90p9JEImUouDQ.jpeg)

To connect a sensor and the microcontroller together, you’ll have to plug them into the Breadboard and use the Jumper wires to connect them.

Remember: everything is cheaper on [eBay](http://ebay.com/) and [AliExpress](https://www.aliexpress.com/). You’ll just have to wait a couple weeks for shipping

### What should I build?

Again — and I can’t stress this enough — it’s way easier to start with a project in mind. Now that you understand what a microcontroller is and how to get one, take a different look at the world around you. What can you control? What can you automate? Once you start to answer those questions, you’ll find a project.

While thinking of projects, [Hackster](https://www.hackster.io/) is your best friend. Hackster has a ton of [ESP8266 projects](https://www.hackster.io/esp) and some cool Arduino projects:

For example, you can live out a childhood dream.

You can even build robots.

The point is, you just need an idea.

Sometimes programming the real world is more fun than programming virtual ones.

### What’s next?

Microcontrollers are only the beginning. You have a world of hardware to explore. Happy Hacking ??

#### Further reading:

[**The Absolute Beginner's Guide to Arduino**](http://forefront.io/a/beginners-guide-to-arduino/)  
[_Over the Christmas break from work I wanted to learn something new. I've been eyeing up Arduino for some time now, and…_forefront.io](http://forefront.io/a/beginners-guide-to-arduino/)

[_Taron Foxworth_](https://twitter.com/anaptfox) _is a hardware hacker and the Developer Evangelist at [Losant](https://www.losant.com). His goal is to translate technology for people to learn, love, and be inspired._

