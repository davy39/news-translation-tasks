---
title: 'UPDATED: Improve Your Bluetooth Project With This Valuable Tool'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-11T15:05:54.000Z'
originalURL: https://freecodecamp.org/news/improve-your-bluetooth-project-with-this-valueable-tool
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/protobuf.jpg
tags:
- name: Bluetooth Low Energy
  slug: bluetooth-low-energy
- name: protocol-buffers
  slug: protocol-buffers
seo_title: null
seo_desc: 'By Jared Wolff

  This post is originally from www.jaredwolff.com

  One of the most confusing things about Bluetooth Low Energy is how data is moved
  around. Depending on your application, your device state may be fairly complex.
  That means having an indiv...'
---

By Jared Wolff

**This post is originally from [www.jaredwolff.com](https://www.jaredwolff.com/how-to-define-your-own-bluetooth-low-energy-configuration-service-using-protobuf/)**

One of the most confusing things about Bluetooth Low Energy is how data is moved around. Depending on your application, your device state may be fairly complex. That means having an individual endpoint for every piece of data is suicide by Bluetooth.

So, what’s he solution?

[Protocol Buffers.](https://developers.google.com/protocol-buffers/)

A protocol buffer is a programatic way to encode/decode optimized structured data. They can be shared and manipulated across almost any platform. Nordic actually uses a variant of it for their DFU service.

There was a lot of buzz words in the first few sentences. Hopefully, by the end of this post you’ll understand exactly what I’m talking about.

In this tutorial, i'll include fully flushed out example code that you can clone and start using immediately. All you need is one of these:

![NRF52 Development Kit](https://www.jaredwolff.com/how-to-define-your-own-bluetooth-low-energy-configuration-service-using-protobuf/images/DSC01544.jpg)

So, how do you use this magical software?

Read on!

P.S. this post is lengthy. If you want something to download, [click here for a a beautifully formatted PDF.](https://www.jaredwolff.com/files/how-to-define-a-protocol-buffer-ble-service-pdf/) (Added bonus, the PDF has all three parts of this series!)


## Install
The first part of the process is to make sure you’ve installed all the correct utilities.  Depending on what programming language will determine what you install and use. In this case I’ll outline the utilities that I have used for several projects in the past using C, Go and Javascript.

`protoc` is the most important utility you’ll have to install here. It's the Protobuf "compiler" which takes your `.proto` and `.options` files and turns them into static code.

1. For Mac, download the appropriate release [here](https://github.com/google/protobuf/releases).
2. Unzip the folder
3. Run `./autogen.sh && ./configure && make` in the folder
4. If you get an error `autoreconf: failed to run aclocal: No such file or directory` install `autoconf` using Homebrew:

`brew install autoconf && brew install automake`

Then, re-run step 3.
1. Then run:

```
make check
sudo make install
which protoc
```

Consider `protoc` the compiler for Protocol Buffers. It can either output raw files or libraries directly. That’s because it’s got Go support built in.

That raw data can also be used to generate static libraries for other languages. That usually requires an extra utility (or utilities). I describe the two that the Dondi Lib project used below.

2. `nanopb` is a python script used to create C libraries that encode/decode your structured data.
  It can be installed by navigating to the [nanopb git repo](https://github.com/nanopb/nanopb) and downloading the appropriate files. The most important pieces to include:

1. `pb_encode.c`, `pb_decode.c` and `pb_common.c`
2. `/generator/nanopb_generator.py`
3. And the `/generator/nanopb/`directory co-located with `nanopb_generator.py`

    `nanopb` is meant for deployment on embedded platforms. It's different from `protoc-c` (the regular C variant) because it is optimized for resource constrained systems like embedded processors. Buffers have finite sizes. There's no memory allocation! Depending on if there's bi-directional communication, you can only import and use the encoding functionality or decoding functionality.

4. `pbjs` uses the output from `protoc` to generate a static javascript library. This is powerful because you can then use it in any javascript application. The best way to install `pbjs` is by running:

      ```
      npm install -g protobufjs
      ```

I've simplified this step a bit in the example code. [Get started by cloning the repos here.](https://www.jaredwolff.com/files/protobuf/)

## Setting up the protocol buffer

Create a file called `command.proto`. You can make the contents of that file what's below:

```
syntax = "proto3";

message event {
  enum event_type {
    command = 0;
    response = 1;
  }
  event_type type = 1;
  string message = 2;
}
```

It may look foreign at first but once you take a deeper look, it’s not that much different than a standard C struct or hash table.

I'm using two types of data in this example: a `string` and `enum` as a type. There are actually a few more which you can read up at the [documentation](https://developers.google.com/protocol-buffers/docs/proto). When compiled, the equivalent c struct looks like:

```
/* Struct definitions */
typedef struct _event {
    event_event_type type;
    char message[64];
/* @@protoc_insertion_point(struct:event) */
} event;
```

Where `event_event_type` is

```
/* Enum definitions */
typedef enum _event_event_type {
    event_event_type_command = 0,
    event_event_type_response = 1
} event_event_type;
```

You can nest as many messages inside each other as your hearts content. Typically though, a message is as small as possible so data transmission is as efficient as possible. This is particularly important for resource constrained systems or LTE deployments where you're charged for *every* megabyte used. **Note:** when elements are not used or defined they are typically *not* included in the encoded Protocol Buffer payload.

Normally, when you create a generic message like this, there is no limit to the size of the string `message`. That option can be set in the `.options` file:

```
event.message	max_size:64
```

This way, the memory can be statically allocated in my microprocessor code at compile time. If the message size is greater than 64 bytes then it will get chopped off in the code (or you'll simply get an error during decode). It's up to you, the software engineer, to figure out the absolute maximum amount of bytes  (or characters) that you may need for this type of data.

You can look at more of the `nanopb` related features at [their documentation.](https://jpa.kapsi.fi/nanopb/docs/concepts.html)

## Generating the appropriate static libraries
In order to make this as easy as possible, I put all the following code into a Makefile. When you make a change to the Protocol Buffer, that every library for every language used gets generated.

If we want to generate a static Go file the command looks like:

```bash
protoc -I<directory with .proto> --go_out=<output directory> command.proto
```
If you've installed the nanopb plugin, you can do something similar to generate C code:

```bash
protoc -I<directory with .proto> -ocommand.pb command.proto
<path>/<to>/protogen/nanopb_generator.py -I<directory with .proto> command
```
The first file creates a generic "object" file. The second actually creates the static C library.

For javascript:

```bash
pbjs -t static-module -p<directory with .proto> command.proto > command.pb.js
```

You can test each of these commands with the `.proto` and `.options` file examples above. I also built this manual process into one command in the example repository. [Get access here.](https://www.jaredwolff.com/files/protobuf/)
## Encoding and Decoding

![Encoding](https://www.jaredwolff.com/how-to-define-your-own-bluetooth-low-energy-configuration-service-using-protobuf/images/data-3432628_1920.jpg)

In the examples below, I show you how to use your freshly compiled static code! This is where the fun begins.

### Encoding using Javascript
Here’s a typical flow that you can follow when using a statically generated javascript library. First, initialize the library.

```
// Import the config message
var protobuf  = require('./command.pb.js');
```

Then create an instance of `event`:

```
// setup command
var event = protobuf.event.create();
event.type = protobuf.event.event_type.command;
event.message = "This is";
```

Then, compile the payload. i.e. turn human readable JSON into nicely packed binary. See below.

```
// make sure it's valid
var err = protobuf.event.verify(event);
if( err != null ) {
   console.log("verify failed: " + err);
   return;
}
```

You'll get errors during this step if your object is malformed or if if you are missing `required` elements. I don't recommend using the `required` prefix when defining your `.proto` file. Any checks for required elements can be easily done in your application code.

Finally, the last step is to encode and turn it into raw bytes:

```
// encode into raw bytes
var payload = protobuf.event.encode(event).finish();
```

You can then use payload and send it over BLE, HTTP or whatever. If there's a communication protocol, you can send this buffer over it!

### Decoding in C
Once the data is received it’s decoded on the embedded end. `nanopb` is confusing. But luckily I have some code here that will work for you:

```
// Setitng up protocol buffer data
event evt;

// Read in buffer
pb_istream_t istream = pb_istream_from_buffer((pb_byte_t *)data, data_len);

if (!pb_decode(&istream, event_fields, &evt)) {
   NRF_LOG_ERROR("Unable to decode: %s", PB_GET_ERROR(&istream));
   return;
}

// Validate code & type
if( evt.type != event_event_type_command ) {
   return;
}
```

First, you create an input stream based on the raw data and the size of the data.

Then, you use the `pb_decode` function. You point the first argument to the input stream. The second to the definition of our Protocol Buffer we’ve been working with. It's located in the `command.pb.h` file.

```
/* Defines for backwards compatibility with code written before nanopb-0.4.0 */
#define event_fields &event_msg
```

The last argument is a pointer to the struct to put the decoded data into. (In this case it's `evt` defined right before `pb_istream_from_buffer` above).

### Encoding in C

Let's now say we're going to reply to the message that was just decoded above. So now we have to create data, encode it and send it back. Here's the process:

```
// Encode value
pb_byte_t output[event_size];

// Output buffer
pb_ostream_t ostream = pb_ostream_from_buffer(output,sizeof(output));

if (!pb_encode(&ostream, event_fields, &evt)) {
   NRF_LOG_ERROR("Unable to encode: %s", PB_GET_ERROR(&ostream));
   return;
}
```

First create a buffer that holds the maximum amount of bytes that your Protocol buffer takes up. This is also defined in your `command.pb.h`. In this case `event_size` is set to `67`. Then, similarly to the decode command, you create a stream and connect it to your buffer. Then finally encode the data by pointing your `evt` struct along with the stream and `event_fields`.

As long as `pb_encode` returns without error, the encoded data has been written to `output`! The structure can be variable length so the best way to handle when sending it is to get the `bytes_written` from `ostream`:

```
NRF_LOG_INFO("bytes written %d",ostream.bytes_written);
```

## Conclusion

Nice you made it! I hope you're starting to grasp the power of Protocol Buffers. Don't worry, it took me a little while to figure it all out. *You too can be a Protocol Buffer master!* ?

If you're not too thrilled with Protocol Buffers, there are other alternatives. I've used [MessagePack](https://msgpack.org) with some success on previous products. It's straightforward and has tons of support for a majority of programming languages.

If you are interested how to roll this into a Bluetooth Low Energy project, stay tuned for Part Two. In Part two, I’ll show you how to set up a very simple Bluetooth Service and Characteristic that will be used to transfer our freshly encoded data to-and-fro.

Also, if you want to see all the code in action, [you can download everything here.](https://www.jaredwolff.com/files/protobuf/)


