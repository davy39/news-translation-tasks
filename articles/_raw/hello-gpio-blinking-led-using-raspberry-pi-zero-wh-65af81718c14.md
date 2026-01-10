---
title: Controlling an External LED using a Raspberry Pi and GPIO pins
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-07T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/hello-gpio-blinking-led-using-raspberry-pi-zero-wh-65af81718c14
coverImage: https://cdn-media-1.freecodecamp.org/images/0*xch19X3RFpIZdFXw.png
tags:
- name: Electronics
  slug: electronics
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: Raspberry Pi
  slug: raspberry-pi
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Shahbaz Ahmed

  In this post we’ll explore Raspberry Pi GPIO pins by creating a “Hello World” GPIO
  program that results in a blinking red LED. We’ll be using the Python programming
  language. I am using a headless Raspberry Pi Zero WH (wireless with ...'
---

By Shahbaz Ahmed

In this post we’ll explore Raspberry Pi GPIO pins by creating a “Hello World” GPIO program that results in a blinking red LED. We’ll be using the Python programming language. I am using a headless Raspberry Pi Zero WH (wireless with soldered headers) with Raspbian Stretch Lite (Raspberry Pi operating system with a minimal image based on Debian Stretch).

I will talk to my headless Pi using `ssh` and transfer necessary files from my Mac to Pi using `scp` commands. I am assuming you have your Raspberry Pi up and running with Raspbian OS installed. If not, then there are lot of articles on the Internet describing how to setup your Pi and install Raspbian, including the official [Raspberry Pi documentation](https://www.raspberrypi.org/documentation/).

Things you’ll need:

* 1 x Raspberry Pi (I am using the Pi Zero WH model)
* 1 x bread board
* 1 x red LED light
* 1 x 330 ohm resistor
* 2 x female to male jumper cable

### GPIO pins configuration

**GPIO** stands for **General Purpose Input Output**. With the help of GPIO pins, a Raspberry Pi can connect and interact with external electronic components. Recent Raspberry Pi models (Pi 3, Pi Zero, Pi W and Pi WH models, and so on) contain 40 GPIO pins. Each pin can turn on or off, or go `HIGH` or `LOW` in electronic terms. If the pin is `HIGH` it outputs 3.3 volts, if the pin is `LOW` it is off.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Zpa1YOQcMlvu-Sxs.png)

In our example, we’ll be using `pin 6` (ground) and `pin 25`. To know more about the GPIO pins in Raspberry Pi, checkout [pinout.xyz](https://pinout.xyz/).

### Setting up the circuit

You should turn the Pi off while building the circuit. We’ll create a circuit as depicted in the diagram below:

![Image](https://cdn-media-1.freecodecamp.org/images/0*xch19X3RFpIZdFXw.png)

**Note**: The resistor in the image is of 220 Ohm, but I have used 330 Ohm in my circuit.

1. Use a female to male jumper cable to connect `pin 6` (Ground) (black cable in the image above) to the breadboard negative row.
2. Use another female to male jumper to connect to connect GPIO `pin 25` to point represented by row `A` and column `12` on the breadboard as shown above (blue cable in the image above).
3. Connect one end of a 330 ohm **resistor** to the negative row (the row that is highlighted in green where the black cable above earlier connected) and connect the other end to the point represented by row `C` column `11` on the breadboard as shown above.
4. The shorter end of the **LED** is the negative end and the longer is the positive end. The longer end should always be connected to the point in the circuit with higher voltage (that is, higher potential). The shorter end of the **LED** is connected to a GPIO `pin 25` (which can output 3.3V) via the blue cable and the longer end is connected to the ground `pin 6` (which is 0V and acts like the negative terminal of the battery) via the black cable with a resistor in between them.

### Resistor

Keeping in mind that I had taken introductory classes on electrical and electronics engineering quite some time ago (4 to 5 years approx.), I had two questions that I needed answers for. Please bear with me for being naive in this context.

1. Why do we need a resistor in our circuit?
2. How do we determine how many Ohms (the measure of electrical resistance) the resistor should be?

A resistor is required to dissipate the extra electrical energy (voltage) from the Raspberry Pi. Raspberry Pi is rated to supply 50mA at 3.3V. Let’s say our red LED can have a forward voltage (forward voltage is the “negative voltage,” used by the LED when it’s on) of around 2V and consumes 4mA current. So the remaining 1.3V should be dissipated by the resistor.

Using Ohm’s law, `V = IR`, `R` = `(3.3V - 2V) / (4/1000)` which comes to around `325 ohms` — so I recommend using a **330 ohm resistor**.

I discovered this from a [Raspberry Pi forum discussion](https://www.raspberrypi.org/forums/viewtopic.php?t=84240).

### Making the LED blink using Python

Now that we have a complete circuit, the next part is to program the GPIO ports to make the magic happen: to get the LED to blink. We will be using the output of GPIO `pin 25` to make the LED blink.

Start your Pi and connect to it using ssh. In the terminal, use the following command to install the Python library `gpiozero`. The `gpiozero` library makes working with GPIO pins and connected external components very simple.

To install the Python library, type `sudo apt-get install python3-gpiozero`.

Now we will run some Python code. Save the code below onto your your Pi file system in a file named `blink1.py`. The script basically turns on the LED connected to `pin 25`, sleeps for 1 second, then turns off the LED, and again sleeps for 1 second. And this is done continuously in a loop until the program is terminated (pressing `ctrl` + `c`).

Now from terminal, go the the directory where the script is saved and run it using the command: `python3 blink1.py`.

You will see the red LED blinking like this:

![Image](https://cdn-media-1.freecodecamp.org/images/0*5v09jlygdroPzBCF.gif)

We can build lots of fun stuff using `gpiozero` using a similar setup. Check out [the documentation](https://gpiozero.readthedocs.io/en/stable/recipes.html) for `gpiozero` which demonstrates some interesting examples. Try building a traffic light system.

_Originally published at [shahbaz.co](http://shahbaz.co) on April 7, 2018._

