---
title: The quick guide to the way computers work for desperate new coders
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-16T07:02:57.000Z'
originalURL: https://freecodecamp.org/news/the-quick-guide-to-the-way-computers-work-for-desperate-new-coders-fcdb34cbe8a9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*j4oOOKFcBCmSOfVlAx5UTA.jpeg
tags:
- name: internet
  slug: internet
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Danielle Ormshaw

  The sole purpose of your computer is to send and receive information in the form
  of numbers — one and zero.

  When I first understood the weight of that concept, I became transfixed. How can
  we create such complex interactions from ...'
---

By Danielle Ormshaw

The sole purpose of your computer is to send and receive information in the form of numbers — one and zero.

When I first understood the weight of that concept, I became transfixed. How can we create such complex interactions from a series of ones and zeros?

I poured over computer science texts, and scoured the internet. I was struggling to understand how it all plugged together. This is the guide I wish I had found months ago, when I first started this journey.

#### Humans communicate using the decimal system

When humans want to communicate using numbers, they use the decimal system. The decimal system has ten digits (0–9), and humans interpret it based on the column those digits appear in. Consider the decimal number 148. When you read this example, you subconsciously follow the steps below:

![Image](https://cdn-media-1.freecodecamp.org/images/dDhLCsHJho2mEfhcyTU6p62DYz7B6uYXYURd)
_Image courtesy of [Danielle Ormshaw](https://twitter.com/SchnucklePi" rel="noopener" target="_blank" title=")._

1. Multiply the right-most number by 10^0.
2. Multiply the middle number by 10^1.
3. Multiply the left-most number by 10^2.
4. Add the outputs from steps 1–3.

Using this system, you were able to extrapolate the correct meaning — one hundred and forty eight.

In the decimal system, we always multiply digits by 10 to the power of something. Every time we add a new column to the left-hand side of the table, that power must increase by one. In this way, we say that the decimal system has a base of 10. Simple enough?

#### Computers communicate using the binary system

When computers want to communicate, they use a similar system. The binary system has two digits (0,1), and we can break it down in the same manner as the decimal system. This time, instead of working with a base of 10, we are working with a base of 2.

Consider the binary number 110. When a computer interprets this binary code, it will follow the steps below:

![Image](https://cdn-media-1.freecodecamp.org/images/On4kpucSuObeC674s2uIY41mDzZYuvPzlwMU)
_Image courtesy of [Danielle Ormshaw](https://twitter.com/SchnucklePi" rel="noopener" target="_blank" title=")._

1. Multiply the right-most number by 2^0.
2. Multiply the middle number by 2^1.
3. Multiply the left-most number by 2^2.
4. Add the outputs from steps 1–3.

Again, every time we add a new column to the left-hand side of the table, we need to increase the power by one.

#### The internet is a physical system, designed to move information

We’ve learned how to use binary code to store information, but how does that work in practice?

The internet is like an Amazon delivery courier. Instead of shipping parcels back and forth, it ships bits. It doesn’t matter if you are sending a photo or a document — every piece of information on the internet is represented in bits. Each bit has a single binary value (zero or one), and eight bits come together to form a byte.

![Image](https://cdn-media-1.freecodecamp.org/images/rke7oIm8BmhDL4tzXCBTkZRlObF829oZFrut)
_Illustration courtesy of [Twitter](https://twitter.com/SchnucklePi" rel="noopener" target="_blank" title="">Danielle Ormshaw</a> on <a href="https://twitter.com/SchnucklePi/status/971362650918670337" rel="noopener" target="_blank" title=")._

When you download a file to your computer, you are likely to see a file size in the kilobyte or megabyte range. The kilobyte is one thousand bytes, and the megabyte is one million bytes.

The transmission of binary information can occur in one of three ways:

1. Electric transmission.
2. Fibre optic transmission.
3. Wireless transmission.

Internet service providers (ISP) supply the physical infrastructure that supports these systems.

#### Every device connected to the internet has a unique address

When you order a parcel from Amazon, the courier will use your address to deliver to the correct place. The internet works in exactly the same way.

When we Google something, we send our request to a unique string of numbers, known as an IP address. These requests will include a multitude of bits and the IP address of the original device. This is like a “return address,” and the recipient can now understand where the request came from.

That said, when we want to visit Google, we don’t type a string of numbers into the browser. So, how do our computers know where to send each request?

#### The internet works via a series of protocols and checkpoints

The domain name system (DNS) converts human readable web addresses into numerical IP addresses. In the event that the DNS doesn’t know the address, it will engage a network of connected servers to find the answer.

![Image](https://cdn-media-1.freecodecamp.org/images/6d9E3Ds1Tgab45xyrutKvKCDDqjDFPHmVjNJ)
_Illustration courtesy of [Twitter](https://twitter.com/SchnucklePi" rel="noopener" target="_blank" title="">Danielle Ormshaw</a> on <a href="https://twitter.com/SchnucklePi/status/971746123298889729" rel="noopener" target="_blank" title=")._

When two devices communicate, they send information in packets. We often need to break information into multiple packets. Each one will contain bytes of the information and both the sending and receiving IP addresses.

Packets move through the network of devices by making use of a traffic management system. Routers track the paths that packets may take, and identify the “cheapest” route. The cheapest route is often defined as the path with the least congestion. When managing packets, routers may also consider non-technical factors, such as international politics.

Packets may take different routes through the network, and often arrive at their destination out of sequence. How does the network handle that?

The transmission control protocol (TCP) acts as an inventory check. If all packets are present, TCP sends an acknowledgement of receipt to the sending device. If not, TCP will “refuse to sign” for the delivery and will request all missing packets.

![Image](https://cdn-media-1.freecodecamp.org/images/M4qSQ2gLbtyVUQAYMRtlChaPOYuvfzV9mD9A)
_Illustration courtesy of [Danielle Ormshaw](https://twitter.com/SchnucklePi" rel="noopener" target="_blank" title=")._

In summary, the domain name server (DNS) translates human readable web addresses into an IP. Information is broken down, transported, and accepted in the form of packets. Packets contain binary information in the form of bits, and electric cables, fibre optic, and wireless networks send these bits between IP addresses.

#### What’s next?

If this post helped you understand the basics, please show your appreciation with a round of applause or by following me on [Twitter](https://twitter.com/SchnucklePi). Happy coding!

