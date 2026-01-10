---
title: What is Raspberry Pi? Specs and Models (2021 Guide)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-08-25T16:17:20.000Z'
originalURL: https://freecodecamp.org/news/what-is-raspberry-pi-specs-and-models-2021-guide
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/Raspberry-Pi-2-Bare-FL-bigger.jpeg
tags:
- name: Internet of Things
  slug: internet-of-things
- name: iot
  slug: iot
- name: Raspberry Pi
  slug: raspberry-pi
seo_title: null
seo_desc: 'By Veronica Stork

  Introduction

  Are you curious about the IoT (Internet of Things?) Have you always wanted to try
  to make your own robot, smart mirror, or bird feeder camera? What about building
  a computer for a fraction of the cost of a commercially ...'
---

By Veronica Stork

## Introduction

Are you curious about the IoT (Internet of Things?) Have you always wanted to try to make your own robot, smart mirror, or bird feeder camera? What about building a computer for a fraction of the cost of a commercially available machine?

If you said yes to any of these questions, you might enjoy playing around with a Raspberry Pi. 

In this article, I'll explain what a Raspberry Pi is (and what it’s not.) Then I'll show you some things you can use it for, and finally, I'll list all of the current models along with their specs.

## What is Raspberry Pi?

A Raspberry Pi is a single board computer (SBC) created in the United Kingdom by the [Raspberry Pi Foundation](https://www.raspberrypi.org/about/). It's a charity that "works to put the power of computing and digital making into the hands of people all over the world."

The first model of the Raspberry Pi was released in 2012, and as of 2021 there have been five generations of the boards. A microcontroller (more about that later), called the Pico was released in early 2021.

### GPIO Pins

Something that sets the Pi apart from your average computer is the set of 40 GPIO (General Purpose Input Output) pins. 

GPIO pins are pretty much exactly what they sound like. They are designed to input and output single bits. This means that you can use them to add all sorts of functionality to your Raspberry Pi using switches, buzzers, lights, sensors, and so on.

### Raspberry Pi HATs

There are a number of add-on boards that you can attach to the Raspberry Pi using the GPIO pins. 

Raspberry Pi HATs (Hardware Attached on Top) are add-on boards designed according to certain specifications. The Raspberry Pi can automatically detect and configure the HATs, making set-up easy.

There is a _huge_ variety of HATs and other add-on boards that you can buy, but here are some notable ones:

* **[PoE+ HAT](https://www.raspberrypi.org/products/poe-plus-hat/)** – Power over Ethernet HAT
* **[Sense HAT](https://www.raspberrypi.org/products/sense-hat/)** – Designed for the [Astro Pi mission](https://astro-pi.org/), the Sense HAT includes a gyroscope, an accelerometer, a magnetometer, and sensors for temperature, humidity, and Barometric pressure.  
* **[Pimoroni Explorer HAT Pro](https://shop.pimoroni.com/products/explorer-hat)** – All-purpose board featuring touch pads, crocodile clip pads, and analog inputs
* **[Adafruit Capacitive Touch HAT](https://www.adafruit.com/product/2340)** – Similar to a [Makey Makey](https://makeymakey.com/), this HAT allows you to use any conductive object to trigger events using Python.

### Raspberry Pi Operating Systems

The Raspberry Pi often runs some form of Linux, but there are a ton of operating systems that you can use. 

On the official website, you will find a list of [operating system images](https://www.raspberrypi.org/software/operating-systems/) available for download. These include the official Raspberry Pi OS, Debian Buster, and Ubuntu (desktop, core, and server.) 

You will also find RetroPie, a specialized gaming platform operating system, and LibreELEC, a lightweight Linux distribution specifically created for use with the open source media player [Kodi](https://kodi.tv/).

### Raspberry Pi VS Arduino

You may have heard of Arduino boards and wondered what the difference is between them and the Raspberry Pi. 

The main difference is that Pis (with the exception of the Pico and the RP2040) are full computers with operating systems. You can connect your Pi to a keyboard, mouse, and monitor and use it like you would use a Mac or PC. 

The Arduino, on the other hand, is a microcontroller. It cannot function independently as a computer, but is programmed using a computer and then used to control things like cameras, lights, robots, and so on. 

As the official Arduino website puts it: “Arduino boards are able to read inputs… and turn it into an output.”

## What is the Raspberry Pi Used For?

Search the internet and you will find a huge array of projects created using Raspberry Pis. 

Common use cases include home automation, gaming consoles, servers, WiFi extenders, streaming devices, weather stations, and home computers. (Fun fact: much of this article was written on a Raspberry Pi.)

During the Covid-19 pandemic, Raspberry Pi's were even used to control [ventilators](https://www.engadget.com/raspberry-pi-ventilators-covid-19-163729140.html) in some hard-hit areas.

## Raspberry Pi Models

All models of Raspberry Pi that are currently in production have 40 GPIO pins. 

This list does not include the Raspberry Pi microcontrollers, the Pico and the RP2040. 

You can find out where to purchase any of these boards on the [Raspberry Pi website](https://www.raspberrypi.org/products/).

| Model | Processor | RAM | Connectivity | USB | HDMI | Power | Price |
| ----- | -------- | ------ | ------------ | ---- | ------------- | ----- | ---- |
| Zero | BCM2835 | 512MB | None | Micro USB OTG | Mini HDMI | Micro USB | $5 |
| Zero W | BCM2835 | 512MB | 802.11 b/g/n wireless LAN | Micro USB OTG | Mini HDMI | Micro USB | $10 |
| Raspberry Pi 1 Model A+ | BCM2835 | 512MB | None | 1x USB 2.0 | Full-size HDMI | Micro USB | $25 |
| Raspberry Pi 1 Model B+ | BCM2835 | 512MB | 100 base ethernet | 4x USB 2.0 | Full-size HDMI | Micro USB | $30 |
| Raspberry Pi 3 Model A+ | BCM2837B0 | 512MB | dual-band wireless, Bluetooth 4.2 | 1x USB 2.0 | Full-size HDMI | 5V DC via Micro USB | $25 |
| Raspberry Pi 3 Model B | BCM2837 | 1GB | ethernet, wireless, BLE | 4x USB 2.0 | Full-size HDMI | 2.1A via Micro USB | $35 |
| Raspberry Pi 3 Model B+ | BCM2837B0 | 1GB | dual-band wireless, Bluetooth 4.2, BLE | 4x USB 2.0 | Full-size HDMI | 5V DC via Micro USB & Power-over-Ethernet (PoE) | $35 | 
| Raspberry Pi 4 Model B | BCM2711 | 2GB, 4GB, or 8GB | Gigabit ethernet, dual-band wireless, Bluetooth | 2x USB 3.0 & 2x USB 2.0 | 2x micro HDMI | 5V DC via USB-C | $35, $55, $75 |
| Raspberry Pi 400 | BCM2711 | 4GB | Gigabit ethernet, dual-band wireless, Bluetooth | 2x USB 3.0 & 1x USB 2.0 | 2x micro HDMI | 5V DC via USB | $70 |

## Conclusion

The Raspberry Pi is an affordable way to explore electronics, hardware, and computer programming. It can be used for a huge variety of projects, from the very silly (like a [hamster powered hamster drawing machine](https://www.raspberrypi.org/blog/hamsters-all-the-way-down/)) to the very important (like [computer labs](https://www.raspberrypi.org/blog/building-computer-labs-in-western-africa/) in developing nations.)

Now that you know the basics, why don't you go out and make something? Whether you hook a Capacitive Touch HAT up to your Raspberry Pi and turn it into a banana piano or install Linux on it and use it to do your homework, I hope you have a great time creating something cool and useful.

