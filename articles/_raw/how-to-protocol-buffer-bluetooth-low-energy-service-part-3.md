---
title: How to Protocol Buffer Bluetooth Low Energy Service Part 3
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-11T16:02:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-protocol-buffer-bluetooth-low-energy-service-part-3
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/Protocol-Buffers-Part-2-2.jpg
tags:
- name: Bluetooth Low Energy
  slug: bluetooth-low-energy
- name: protocol-buffers
  slug: protocol-buffers
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: 'By Jared Wolff

  This post is originally from www.jaredwolff.com

  In Part 1 we’ve learned the anatomy of a Protocol Buffer. In Part 2 we’ve learned
  how a Bluetooth Low Energy Service gets pieced together on the Nordic NRF52 SDK.
  This final post brings t...'
---

By Jared Wolff

**This post is originally from [www.jaredwolff.com](https://www.jaredwolff.com/how-to-protocol-buffer-bluetooth-low-energy-service-part-3/)**

In [Part 1][part1] we’ve learned the anatomy of a Protocol Buffer. In [Part 2][part2] we’ve learned how a Bluetooth Low Energy Service gets pieced together on the Nordic NRF52 SDK. This final post brings together all the elements in an end-to-end working example.

Let’s get going!

P.S. this post is lengthy. If you want something to download, [click here for a a beautifully formatted PDF.](https://www.jaredwolff.com/files/how-to-define-a-protocol-buffer-ble-service-pdf/) (Added bonus, the PDF has all three parts of this series!)

## Setting Everything Up

![Goose attack](https://www.jaredwolff.com/how-to-protocol-buffer-bluetooth-low-energy-service-part-3/images/Untitled-6880beab-c5c2-4184-9012-4a6e68bcebc8.png)

Go look at the `Readme.md` in each of the example repositories. (You will have to clone the repositories, [sign up here to get the code][code]).

I’ve made the setup for the firmware dead simple. For the javascript side, it’s a bit more hairy but’ doable! I’ll also include the instructions here as well:

### Firmware Setup (For Mac)

1. Initialize the full repository (there are submodules!): `git submodule update --init`
2. Install `protoc` using Homebrew: `brew install protobuf`
3. Run `make sdk`. This will download your SDK files.
4. Run `make tools_osx`. This will download your ARMGCC toolchain (for Mac). For other environments see below.
5. Run `make gen_key` once (and only once)! This will set up your key for DFU.
6. Run `make` and this will build your bootloader and main app.

**Note:** You only have to do steps 1-5 once.

### Javascript App Setup (For Mac)

**Prerequisite:** you will need Xcode command line tools. You can get those [here](https://developer.apple.com/download/more/).

1. Clone this repo to a place on your computer
2. Make sure you have [nvm installed](https://github.com/nvm-sh/nvm/blob/master/README.md)
3. Run `nvm install v8.0.0`
4. Run `nvm install v10.15.3`
5. Run `nvm use v8.0.0`
6. Run `yarn` (if you don’t have yarn `npm install yarn -g`)
7. Once installed, run `nvm use v10.15.3`
8. Then run `node index.js` to start the example

Using NVM helps mitigate a compile issue with the Bluetooth library. You mileage may vary on this one.

## How the heck does this work?

In this project, the Protocol Buffer has two functions. The first as a “command” to the bluetooth device. Secondly, a “response” to that command from the device.

Our example javascript app command uses “This is” as the payload. With the power of some string operations, let's make a full sentence out of it!

The series of events looks something like this:

1. The test app connects and sends that data using our Bluetooth Low Energy service.
2. On the firmware decodes the message.
3. The firmware modifies the original data by adding “ cool.” Resulting in "This is cool"
4. The firmware encodes the payload and makes the data available for reading.
5. The app finally reads the characteristic, decodes and displays the result!

Seems complicated but there's some benefits to this:

1. In Protocol Buffers, data structures are well defined. This means that it has some great error checking abilities. If you're using any type of data structure you may have to code your own data validation.
2. Encoding and decoding is simple and straight forward. You can encode same data on different platforms and always get the same decoded result.

Want to get the example up and running? Seeing is believing after all. Let's do this.

## Is This Thing On?

![Phone in hand running NRF connect](https://www.jaredwolff.com/how-to-protocol-buffer-bluetooth-low-energy-service-part-3/images/Untitled-c72fcf71-f0db-49e5-92d7-44fe601e75fa.png)

Once you're done with the setup (above), let's get this firmware programmed! Lucky for you it's only two quick steps!

1. Plug in your NRF52 DK board
2. Run `make flash_all`. (This compiles and flashes *all* the code for the project.)

Once flashed, the easiest way to know if things are working is when Led 1 is blinking. That means it’s advertising and ready for a connection.

![NRF52 DK](https://www.jaredwolff.com/how-to-protocol-buffer-bluetooth-low-energy-service-part-3/images/Untitled-6c58e8c5-d005-4b61-a32b-29eea61b1ce7.png)

Let’s make sure it’s advertising correctly though. You can grab a tool like NRF Connect for [iOS](https://itunes.apple.com/cn/app/nrf-connect/id1054362403?l=en) or Android. Or, you can grab LightBlue. (Also available for [iOS](https://apps.apple.com/ru/app/lightblue-explorer/id557428110?l=en) and Android)

Open up one of the app and scan for advertising devices. You’ll be looking for **Nordic_Buttonless**.

![BLE Apps scanning](https://www.jaredwolff.com/how-to-protocol-buffer-bluetooth-low-energy-service-part-3/images/Untitled-062f5e84-ec22-4525-a591-4330a55fe30f.png)

Now let’s connect and double check our connectable services & characteristics:

![BLE Apps showing services](https://www.jaredwolff.com/how-to-protocol-buffer-bluetooth-low-energy-service-part-3/images/Untitled-0466566a-1d8a-4e8b-a1c9-f2f76faa116b.png)

As you can see there are two services. One is Nordic’s DFU service. The other is our Protocol Buffer service!

You can compare `PROTOBUF_UUID_BASE` in `ble_protobuf.h` with the UUID of the “Unknown Service”. Nordic’s chips are Little Endian while the data here is Big Endian format. (i.e. you’ll have to reverse the bytes to see that they’re the same!)

You can even click in further to see the characteristics in NRF Connect. In the case of LightBlue, the characteristic UUIDs are already shown.

## Using the Javascript App

So, once we’re up and advertising, it’s time to run the app.

![Bluetooth javascript app results](https://www.jaredwolff.com/how-to-protocol-buffer-bluetooth-low-energy-service-part-3/images/Untitled-7e92193a-4dbe-4e08-9ebe-ee41be501580.png)

Simply change to the `ble-protobuf-js` directory and run `node index.js`

If you've installed everything correctly, you should start seeing output like:

    example started
    scanning
    peripheral with ID 06f9b62ec5334454875b9f53d2f3fa74 found with name: Nordic_Buttonles

It should then immediately connect and send data to the device. It should receive the response immediately and print it to the screen.

    connected to Nordic_Buttonles
    Sent: This is
    Received: This is cool.

Bingo!

## You’ve made it!

? Congrats if you made it this far through the tutorial. You should now be feeling confident enough to start playing with the software code. Maybe you’ll cook up something cool?

Here’s links to some resources that you may find handy.

- [Protocol Buffer documentation](https://developers.google.com/protocol-buffers)
- [NanoPB](https://www.github.com/nanopb/nanopb) - (the implementation of Protocol Buffers we used for this project)
- [Nordic SDK Documentation](https://www.nordicsemi.com/DocLib/Content/SDK_Doc/nRF5_SDK/v15-2-0/index)
- Again, here are the links to [Part 1][part1] and [Part 2][part2]
- If you haven’t already, [get all the code for this project][code]

## Conclusion

Protocol Buffers are quite versatile and convenient. Using them with Bluetooth Low Energy service is one way that you can take advantage. As the connected world of IoT continues to expand, I have no doubt that we'll be seeing more use cases in the future!

I hope this has inspired you to incorporate Protocol Buffers into your own project(s). Make sure you [download the sample code][code] and get started right now.

Has this tutorial been useful for you? Let me know what you think.

[code]: https://www.jaredwolff.com/files/protobuf
[part1]: https://www.jaredwolff.com/how-to-define-your-own-bluetooth-low-energy-configuration-service-using-protobuf
[part2]: https://www.jaredwolff.com/how-to-protocol-buffer-bluetooth-low-energy-service-part-2


