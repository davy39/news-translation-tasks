---
title: How to Handle Errors in Computer Networks
subtitle: ''
author: Omer Rosenbaum
co_authors: []
series: null
date: '2023-01-18T16:05:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-handle-errors-in-computer-networks
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/Copy-of-Computer-Networks-Hub-Switch.png
tags:
- name: computer network
  slug: computer-network
- name: computer networking
  slug: computer-networking
- name: error
  slug: error
- name: error handling
  slug: error-handling
seo_title: null
seo_desc: 'There are some magical things about the Internet, and one thing in particular
  is that it works. In spite of so many obstacles, we can deliver our packets over
  the globe, and do so fast.

  Even more specifically, one amazing thing about the Internet is ...'
---

There are some magical things about the Internet, and one thing in particular is that it works. In spite of so many obstacles, we can deliver our packets over the globe, and do so fast.

Even more specifically, one amazing thing about the Internet is its ability to handle errors. 

What do I mean by errors? When a packet or a frame is received by a machine, we say it contains an error if the data that had been sent is not the data that was received. For instance, a single `1` was mistakenly received as a `0` after its transmission. 

This can happen due to many different reasons. Perhaps there was some disturbance in the wire where the data was transmitted – say, a child rode her bicycle over the wire. Perhaps there was some collision in the air as many people transmitted at once. Maybe it was a device's error.

Regardless of the specific reason, you still get valid data on the Internet. Without handling errors, you may read the last sentence and instead of `errors` read `errbbb`. Weird, isn't it? So how does the Internet handle errors?

There are two main approaches for handling errors – detection, and correction. We shall start by describing detection, and then talk about correction.

# What is Error Detection?

When dealing with error detection, we are looking for a boolean result – `True`, or `False`. Is the frame/packet valid, or not. That is all. We don’t want to know where the error occurred. If the frame is invalid, we will simply drop it.

So when the receiver receives a frame, they will determine whether an error has occurred. If the frame is valid, they will read it. If the frame contains errors - the receiver will drop it.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-84.png)
_Error Detection: we only want to know if the frame/packet is valid or not. ([Source: Brief](https://www.youtube.com/watch?v=H_bYtVDF6T4&amp;ab_channel=Brief))_

One method for error detection is using a **checksum**. A common implementation of a checksum is called **CRC – Cyclic Redundancy Check**. 

In this post we will not trouble ourselves with the mathematical implementation of CRCs in the real world (if you're interested, check out [Wikipedia](https://en.wikipedia.org/wiki/Cyclic_redundancy_check)). Rather, we'll simply try to understand the concept. To do so, let’s implement a very simple checksum mechanism ourselves.

Consider a protocol for transmitting 10-digit phone numbers between endpoints. This protocol is extremely simple: each packet includes exactly 10 bytes, each one representing a digit. For example, a packet might include the following digits:

`5551234567`

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-85.png)
_A packet with a payload of 10 digits ([Source: Brief](https://www.youtube.com/watch?v=H_bYtVDF6T4&amp;ab_channel=Brief))_

For simplicity's sake, we will omit the headers of the packet and focus solely on the payload. 

Now, we will add a checksum. Say that we **add** all the digits. So in this example, we would calculate `5` + `5` +`5` +`1`+… all the way through `7`. We would get `43`. This would be our checksum value.

Now, the sender won’t only send the phone number, but also the checksum value right after it. In this example, the sender would send:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-86.png)
_The packet's data is followed by a checksum. ([Source: Brief](https://www.youtube.com/watch?v=H_bYtVDF6T4&amp;ab_channel=Brief))_

Now, as the receiver, you can do the same thing. You will read the phone number, and calculate the checksum. You will add the digits, and get `43`. 

Since you've received the correct result (that is, your calculation based on the data matches the checksum value sent in the packet), you can assume that the frame is valid.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-89.png)
_The sender compares their calculated checksum value and the checksum in the packet. If the values match, the packet is assumed to be valid ([Source: Brief](https://www.youtube.com/watch?v=H_bYtVDF6T4&amp;ab_channel=Brief))_

What happens in case of an error? 🤔

Let’s say, for instance, that the digit `2` was replaced by an `8`. Now, even though the sender sent the same stream as before ( `555123456743` ), you, as the receiver, see something a bit different:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-90.png)
_A packet containing an error ([Source: Brief](https://www.youtube.com/watch?v=H_bYtVDF6T4&amp;ab_channel=Brief))_

Now, you are calculating the checksum, adding all the digits. You get `49`. Since this value is different from the checksum value specified in the original frame, `43`, the frame is considered to be invalid and you drop it.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-91.png)
_The sender compares their calculated checksum value and the checksum in the packet. If the values don't match, the packet is assumed to be invalid ([Source: Brief](https://www.youtube.com/watch?v=H_bYtVDF6T4&amp;ab_channel=Brief))_

Are there problems with this method? 🤔

Yes, there are. Consider, for example, what happens if there are two errors – and instead of the original stream ( `555123456743` ), you receive the following:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-92.png)
_A packet received with two errors, resulting in the stream `456123456743` ([Source: Brief](https://www.youtube.com/watch?v=H_bYtVDF6T4&amp;ab_channel=Brief))_

What happens when you add the digits?

Even though the digits are not the same as the original packet, the checksum will remain correct, and the frame will be regarded as valid.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-93.png)
_Despite the errors, the checksum value happens to be correct, resulting in a false assumption that the packet is valid ([Source: Brief](https://www.youtube.com/watch?v=H_bYtVDF6T4&amp;ab_channel=Brief))_

Real checksum functions, such as CRCs, are of course much better implemented than the one in our example – but in extremely rare cases, such problems may occur. 

Notice that using this kind of method, error detection, we don’t know where the problem occurred, but only whether the frame is valid or not. If the checksum value is invalid, we assume that the frame is invalid and drop it.

# What is Error Correction?

As mentioned earlier, detection is not the only way to handle errors. Another approach might be to find the error and correct it. How can we do that?

An extremely simple way would be to transmit the data many times – let’s say, three times. For example, the stream `5551234567` would be transmitted as follows:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-94.png)
_Sending the same data multiple times ([Source: Brief](https://www.youtube.com/watch?v=H_bYtVDF6T4&amp;ab_channel=Brief))_

So we basically sent the data three times.

Now, in case of an error in one digit, the receiver can look at the other two digits, and choose the one that appears two times out of three.

So, for instance, if we had a problem and `2` was replaced with an `8`, the receiver would get this stream:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-95.png)
_An error in one of the occurrences of the data ([Source: Brief](https://www.youtube.com/watch?v=H_bYtVDF6T4&amp;ab_channel=Brief))_

Now, as a receiver, you can say: “I have `2`, `8`, `2`… so it was probably `2` in the original message”.

Is this problematic? Well, in some rare cases, we might get the same error twice. So it is possible, even though unlikely, that two of the original twos have been received as eights.

So while the sender sent this stream:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-94.png)
_Sending the same data multiple times ([Source: Brief](https://www.youtube.com/watch?v=H_bYtVDF6T4&amp;ab_channel=Brief))_

The first `2` was mistakenly read as an `8`, and also the second `2` was received as an `8`:

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-96.png)
_Two identical errors; Rare, but possible ([Source: Brief](https://www.youtube.com/watch?v=H_bYtVDF6T4&amp;ab_channel=Brief))_

 Now, it looks as if the original message included an `8`, and not a `2`.

What can you do in order to lower the probability of such scenario?

The most simple solution would be to simply send the data even more times. Let’s say, five times. So now we duplicate all the data, and send it 5 times in total… 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-97.png)
_Sending the data five(!) times ([Source: Brief](https://www.youtube.com/watch?v=H_bYtVDF6T4&amp;ab_channel=Brief))_

Now, say that two errors occurred, and again two of the `2` digits were replaced with `8`s.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-98.png)
_Two identical errors; Rare, but possible ([Source: Brief](https://www.youtube.com/watch?v=H_bYtVDF6T4&amp;ab_channel=Brief))_

Clearly, it is very unlikely to get the same error twice, but even in this case, we still get `2` three times, so as the receiver you can tell, with a high probability, that the original message contained a `2`, rather than an `8`.

## What's the Overhead?

Now would be a good time to introduce the term **overhead**. When we say overhead, we basically mean data or time needed to convey the actual message. Let’s first understand what this term means in general, and then consider it in the context of handling errors.

Let’s say that I have a lesson to teach in my university. My goal is to teach the lesson itself, which is also called the **payload** in that context – that is, the actual data or message I would like to convey.

In order to teach the lesson, or to convey the payload, I first have to physically get to the university – so I get out of my home, walk to the bus station, wait for the bus, take the bus, get off the bus, walk to the building, wait for the lesson to start – and only then do I actually get to teach the lesson. 

This entire process is **overhead** that I have to pay in order to deliver the **payload**, in this case – to teach the lesson.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-99.png)
_Overhead and Payload are two extremely important terms in Computer Networks ([Source: Brief](https://www.youtube.com/watch?v=H_bYtVDF6T4&amp;ab_channel=Brief))_

The same applies in computer networks. Our **payload** is the data, and there is always some **overhead** associated with sending it. 

## Back to Handling Errors

In the context here – sending the data three times, as suggested earlier, means that for every byte of payload we have two bytes of overhead. If we send the data five times, then for every byte of payload, we have four bytes of overhead. That’s a LOT!

Consider error _detection_, on the other hand. In our example protocol for sending phone numbers, how much overhead did we have?

Recall that for every ten-digit phone number, that is ten bytes, we included a two-digit checksum value. In other words, we had two bytes of overhead for ten bytes of payload. It is clear that in our example, error detection yields much smaller overhead in comparison to error correction.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-100.png)
_In the sample protocol, for every ten-digit phone number (ten bytes of payload), we included a two-digit checksum value (two bytes of overhead) ([Source: Brief](https://www.youtube.com/watch?v=H_bYtVDF6T4&amp;ab_channel=Brief))_

There are better ways to achieve error correction with high accuracy than to simply send the data so many times, but they are more complicated and out of scope for this post. Even with very complicated error correction techniques, they still require lots of overhead when compared to error detection.

Also, notice that except for the bytes sent as overhead in case of error correction, error detection is much simpler. 

# Error Correction vs Error Detection – Which is Better?

We already concluded that error detection is simpler, and with a smaller payload compared to error correction.

### So, when would we prefer error correction?

One case might be when we have a one-way link. That is, a network where we can only transfer data in one direction. 

For example, say you have a secret agent that you need to send a message to. The agent knows that they need to look up to the sky at exactly midnight, and they will see a series of flashes indicating the secret message. 

The secret agent cannot reply, or their location and identity will be revealed. In addition, you don’t want to send the message over and over again, as not to draw much attention, and to make it harder for someone to intercept the message.

In this case, you definitely want your agent to receive the exact message that you’ve sent. Consider a case where you want to send them the message “do not place the bomb”. 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-101.png)
_A sensitive message for a secret agent ([Source: Brief](https://www.youtube.com/watch?v=H_bYtVDF6T4&amp;ab_channel=Brief))_

Of course, you don’t want to risk the unfortunate scenario of the agent reading the message as “do **now** place the bomb”, due to an error.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-102.png)
_An error may change the meaning of the message substantially ([Source: Brief](https://www.youtube.com/watch?v=H_bYtVDF6T4&amp;ab_channel=Brief))_

If you use error _detection_, the agent might be aware that the message they received is invalid in case of an error, but they won’t be able to tell you that they need you to send the message again. As you want the agent to be able to read your message correctly and without sending any data back to us, error correction is preferred.

So, one-way link is one case where we prefer error correction. What about other cases?

Sometimes you just _can’t_ send the data again, perhaps because it has been erased from the memory of your machine. That is, the data is deleted right after it has been sent. In this case, you'd clearly prefer error correction, as sending the data again, as we would do with error detection, is just impossible.

Also, if sending the data again is possible, but extremely expensive, error correction may be preferable. 

For example, if you send a message to the moon, say, with a spaceship – it might be really expensive to send it over again in case of an error. Using error correction, you send the data only once and the receiver should be able to deal with it, even if an error occurred.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-103.png)
_Cases where correction is preferred ([Source: Brief](https://www.youtube.com/watch?v=H_bYtVDF6T4&amp;ab_channel=Brief))_

In general, we prefer error correction when retransmitting the data is costly or impossible. 

### When would we prefer error detection?

Well, in case we can retransmit the data, we usually prefer error detection since it comes with very little overhead compared to error correction. Especially, when sending the data is relatively cheap.

For example, on the Internet, if an error occurs when you send a frame, no problem – you can simply send it again! 

For example, when I covered [the Ethernet protocol in a previous post](https://www.freecodecamp.org/news/the-complete-guide-to-the-ethernet-protocol/), I mentioned that Ethernet protocol uses change detection, namely `CRC32` – that is, 32 bits (or 4 bytes) of a checksum for every frame. 

Note that it doesn’t mean that error detection is simply better. It just better fits the Internet than error correction. As mentioned before, error correction is preferable in other cases.

# Wrapping Up

In this tutorial, we discussed various methods for handling errors. We looked at **error detection**, where we only know whether a frame is valid or not. We also considered **error correction**, where the receiver can restore the correct value of an erroneous frame. We also introduced the term **overhead**. 

We then understood why we use error detection on the Internet, rather than error correction. Stay tuned for more posts in this series about Computer Networks 💪🏻

## **About the Author**

[Omer Rosenbaum](https://www.linkedin.com/in/omer-rosenbaum-034a08b9/) is [Swimm](https://swimm.io/)’s Chief Technology Officer. He's the author of the Brief [YouTube Channel](https://youtube.com/@BriefVid). He's also a cyber training expert and founder of Checkpoint Security Academy. He's the author of [Computer Networks (in Hebrew)](https://data.cyber.org.il/networks/networks.pdf). You can find him on [Twitter](https://twitter.com/Omer_Ros).

## **Additional Resources**

* [Computer Networks Playlist - on my Brief channel](https://www.youtube.com/playlist?list=PL9lx0DXCC4BMS7dB7vsrKI5wzFyVIk2Kg)
* [CRC - Wikipedia](https://en.wikipedia.org/wiki/Cyclic_redundancy_check)
* [The Complete Guide to Ethernet Protocol](https://www.freecodecamp.org/news/the-complete-guide-to-the-ethernet-protocol/)

