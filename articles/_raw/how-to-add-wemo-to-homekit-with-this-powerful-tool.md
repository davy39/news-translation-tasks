---
title: How To Add Wemo to Homekit With This Powerful Tool
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-03T21:42:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-wemo-to-homekit-with-this-powerful-tool
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/Copy-of-Dashboard.png
tags:
- name: smart home
  slug: smart-home
seo_title: null
seo_desc: 'By Jared Wolff

  This post is originally from www.jaredwolff.com

  I’ve been nerding out. It’s something I just can’t stop sometimes.

  Most recently working on making our home more connected and efficient. Part of the
  effort was experimenting with some We...'
---

By Jared Wolff

**This post is originally from [www.jaredwolff.com](https://www.jaredwolff.com/how-to-deploy-homebridge-on-raspberry-pi-w-resin/)**

I’ve been nerding out. It’s something I just can’t stop sometimes.

Most recently working on making our home more connected and efficient. Part of the effort was experimenting with some Wemos I had purchased off of eBay about a month ago. The Wemo app works alright but there’s definitely more to be desired there. (Plus it makes me cringe to think every Wemo is running DDWRT)

The main problem? Wemo doesn’t support Apple Homekit.

So I got to researching and found the [Homebridge](https://github.com/nfarina/homebridge) project to be just what I was looking for. Basically, it emulates a device that operates on the HAP protocol that Apple supports for Homekit. Within Homebridge, you can configure as many devices via as many different interfaces you could imagine. Deploying it to a Raspberry Pi, or similar, can be troublesome and wrought with errors. So why not take a different approach?

_Enter Resin OS._

Some advantages of Resin OS are:

- Deploying a pre-optimized image for the Yocto platform
- No configuring of any Linux anything (except for the config.json)
- Get up and running in a few minutes (mostly flashing and container initialization)

I originally played around with Resin’s online platform which shows some promise. For those developers who don’t want to spend time writing code for OTA updates and building Yocto images manually, you should definitely take a look at Resin.io.

(By the way, I have no affiliation with Resin, I think they’ve done a great job and they’ve contributed to the community significantly with their open source tools: [http://resinos.io](http://resinos.io/) , [https://etcher.io](https://etcher.io/) , [https://www.balena.io](https://www.balena.io/) )

![HomeKit on iPhone](https://www.jaredwolff.com/how-to-deploy-homebridge-on-raspberry-pi-w-resin/images/1*duqqYCYgcr1F3f8MNkj0Sg.jpg)

_So how do I get a Wemo working with Homekit?_

Resin themselves have some fantastic documentation. I barely had to look anywhere when error messages came up when developing my first crack at the Docker container. (I was originally using the _slim_ image which does not have all the needed utilities that Homebridge requires, easier to just use the _latest_ image instead)

The instructions are as follows:

1.  Install dependencies. On Mac, _Node_ is the only thing you may need to install. Homebrew works best here.

    ```
    brew install node
    ```

2.  Download and install the resin-cli:

    ```
    npm install —global —production resin-cli
    ```

3.  Download your image from the [download link](https://resinos.io/#downloads) if you haven’t already.
4.  Modify the image to your liking by using the cli.

    ```
    $ sudo resin local configure ~/Downloads/resin.img
    ? Network SSID Wolff Den
    ? Network Key This is not our password.
    ? Do you want to set advanced settings? Yes
    ? Device Hostname resin
    ? Do you want to enable persistent logging? no
    Done!
    ```

5.  “Flash” the image to an SD card. Make sure you have a free device to write to!

    ```
    $ sudo resin local flash ~/Downloads/resin.img
    Password:
    ? Select drive (Use arrow keys)
    ❯ /dev/disk1 (32 GB) - RESIN
    ```

6.  Wait for the process to complete and then eject the card. Pop it into the device you’ve configured the image for.
7.  Once booted, you should be able to ping the device.

    ```
    ping resin.local
    PING resin.local (192.168.7.45): 56 data bytes
    64 bytes from 192.168.7.45: icmp_seq=0 ttl=64 time=9.004 ms
    64 bytes from 192.168.7.45: icmp_seq=1 ttl=64 time=6.411 ms
    64 bytes from 192.168.7.45: icmp_seq=2 ttl=64 time=4.337 ms
    64 bytes from 192.168.7.45: icmp_seq=3 ttl=64 time=4.374 ms
    ```

8.  Modify the config.json file to your liking. Highly suggest changing the pin to something different as this is the one that Homebridge uses in their examples.
9.  Also, feel free to modify the Dockerfile to match your needs. In this example the only thing that you may want to change is the image name. By default I have hummingboard-node:latest as the main image.
10. You can now push the included Homebridge Docker file and associated files directly to your embedded device.

    ```
    sudo resin local push resin.local —source .
    ```

    _Note: this will take several minutes as it will be building the docker image on the embedded device. This takes much less time using the Resin.io platform as it builds on your local machine and then sent to the embedded device as a complete image_

11. Wait to see the output from Homebridge indicating it’s running.
    rdt push completed successfully!

    ```
    Streaming application logs..
    *** WARNING *** The program ‘node’ uses the Apple Bonjour compatibility layer of Avahi.
    *** WARNING *** Please fix your application to use the native API of Avahi!
    *** WARNING *** For more information see <http://0pointer.de/avahi-compat?s=libdns_sd&e=node>
    *** WARNING *** The program ‘node’ called ‘DNSServiceRegister()’ which is not supported (or only supported partially) in the Apple Bonjour compatibility layer of Avahi.
    *** WARNING *** Please fix your application to use the native API of Avahi!
    *** WARNING *** For more information see <http://0pointer.de/avahi-compat?s=libdns_sd&e=node&f=DNSServiceRegister>
    [2017-11-2 02:09:43] Loaded plugin: homebridge-platform-wemo
    [2017-11-2 02:09:43] Registering platform ‘homebridge-platform-wemo.BelkinWeMo’
    [2017-11-2 02:09:43] —
    [2017-11-2 02:09:43] Loaded config.json with 0 accessories and 1 platforms.
    [2017-11-2 02:09:43] —
    [2017-11-2 02:09:43] Loading 1 platforms…
    [2017-11-2 02:09:43] [WeMo Platform] Initializing BelkinWeMo platform…
    Scan this code with your HomeKit App on your iOS device to pair with Homebridge:

        ┌────────────┐
        │ 031-45-154 │
        └────────────┘

    [2017-11-2 02:09:43] Homebridge is running on port 51826.
    [2017-11-2 02:09:43] [WeMo Platform] Found: Master Den [123456789ABC]
    [2017-11-2 02:09:43] [WeMo Platform] Found: Jarchel Den [123456789BAC]
    [2017-11-2 02:09:43] [WeMo Platform] Found: Front Door Light [123456789CBA]
    [2017-11-2 02:09:44] [WeMo Platform] Jarchel Den - Get state: On
    ```

12. Pop open your phone and look for an available accessory in HomeKit. You will likely have to tap on “Don’t Have a Code or Can’t Scan?” and enter the number manually.

    ![Camera add accessory](https://www.jaredwolff.com/how-to-deploy-homebridge-on-raspberry-pi-w-resin/images/1*UuC6kIPSdoqRwc1nxssJ0g.jpg)

    ![Add accessory](https://www.jaredwolff.com/how-to-deploy-homebridge-on-raspberry-pi-w-resin/images/1*xEiX3rxFoTnR4uuZNNR_8Q.jpg)

13. Add your accessory by entering the passcode displayed earlier.

    ![Add accessory with code.](https://www.jaredwolff.com/how-to-deploy-homebridge-on-raspberry-pi-w-resin/images/1*GerWvbaN_jAiXQlHKRaP3Q.jpg)

    ![Homebridge added success!](https://www.jaredwolff.com/how-to-deploy-homebridge-on-raspberry-pi-w-resin/images/1*KcnojEomHxORpWHtCYC2yg.jpg)

Congrats! All your Wemo devices should show up now. Enjoy using Siri with your Wemo devices.

![Default screen](https://www.jaredwolff.com/how-to-deploy-homebridge-on-raspberry-pi-w-resin/images/1*dHFYz4MWLa5RKIP7w9O67w.jpg)


Found this tutorial useful? [Here are some of my other Raspberry Pi related posts.](https://www.jaredwolff.com/tags/raspberry-pi/)

