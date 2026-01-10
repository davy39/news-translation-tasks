---
title: What is the Five Layers Model? The Framework of the Internet Explained
subtitle: ''
author: Omer Rosenbaum
co_authors: []
series: null
date: '2022-10-17T13:37:19.000Z'
originalURL: https://freecodecamp.org/news/the-five-layers-model-explained
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/d.png
tags:
- name: computer network
  slug: computer-network
- name: computer networking
  slug: computer-networking
seo_title: null
seo_desc: "Computer Networks are a beautiful, amazing topic. Networks involve so much\
  \ knowledge from different fields, from physics to algorithms. \nWhen dealing with\
  \ Computer Networks, there is one framework that puts everything into place – and\
  \ that is the lay..."
---

Computer Networks are a beautiful, amazing topic. Networks involve so much knowledge from different fields, from physics to algorithms. 

When dealing with Computer Networks, there is one framework that puts everything into place – and that is the layers model. 

In this post you'll learn _why_ we need layers, as well as _what_ the five layers model is. You will also understand the role of each layer in this model. 

# Why Layers?

Imagine you are given the task to design and implement the Internet! Where do you start? What do we actually want from a network, and an important one such as the Internet? 

Well, we actually want quite a lot of things. To name a few:

* We want it to be **fast** – that is, allow fast communication. We don’t want to wait long for a message to get from one host to another.
* It should also be **reliable** – when sending a message, we want the receiver to actually receive it.
* The network should be **extendable** – that is, allow more devices to join. We wouldn’t want to start with two computers, and then not bee able to add a third one.
* The network should support **different devices and connections** – it should be able to connect a wired PC, wireless laptop, and a cellphone, for example.

And this is just a partial list.

So, how do we go about implementing the internet when we want to achieve so many different things?

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-58.png)
_Computer Networks are complex (Source: [XKCD](https://xkcd.com/2259/))_

In order to simplify things and make networks flexible, the communication is divided into **layers**.

Each layer has its own responsibility. It provides services to an upper layer, and uses services provided by a lower layer.

Consider an example network consisting of three devices:

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-51.png)
_An example network with three devices (Source: [Brief](https://www.youtube.com/watch?v=iHp5J_f_ToQ&amp;ab_channel=Brief))_

We have two layers:

**Layer Alpha** is responsible for transmitting data between hosts that are directly connected to each other. In the diagram above, it's between hosts A and B, or between hosts B and C.

**Layer Beta** is responsible for transmitting data between distant hosts. In the diagram, it's between hosts A and C.

What did we gain from this division? We gained a lot of **flexibility**.

Each layer can be developed and implemented by different people. The upper layer doesn’t care about the implementation of the lower layer, and vice versa.

For instance, the connection between hosts A and B could be a WiFi connection, while the connection between B and C could consist of a carrier pigeon. These are (completely) different implementations of Layer Alpha. 

Notice that this way also enables us to have different specializations and expertise – an expert in training carrier pigeons does not necessarily have to be qualified at building solid WiFi network cards, or vice versa.  


![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-52.png)
_The Alpha Layer may have different implementations on the same network (Source: [Brief](https://www.youtube.com/watch?v=iHp5J_f_ToQ&amp;ab_channel=Brief))_

Developers of Layer Beta don’t need to bother themselves with this difference. At this layer, host A needs to know that in order to reach host C, it first needs to send his message to host B, rather than, say, host D. Then, host B will forward it to host C.

This way, Layer Beta is only responsible for finding the route to send the message. It uses the service provided by Layer Alpha – transmitting data between directly connected hosts.

In general, networks are very complicated, and have various requirements. Dividing the communication into layers will allow us to simplify things and make communication more flexible.

Now that you understand _why_ we need layers, we can go on to learn about the layers that are actually used in networks. 

# What is the Five Layers Model?

There have been a few layer models proposed along the years – most notably, the five layers model, the 7 layers model (aka OSI model), or the 4 layers model (aka the TCP/IP model). 

They are way more similar than different, and I choose to focus on the five layers model as it is the most practical of all – and best describes the way the Internet actually works.

## The First Layer – The Physical Layer

The first layer is responsible for **transmitting a single bit** – 0 or 1 – over the network.

To get some intuition as to what this layer is responsible for, consider the time of transmission. Assume that we have some kind of cable to transmit our data, and we use `+5` Voltage to transmit `1`, and `-5` Voltage to transmit `0`. What bits does the following diagram represent?

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-53.png)
_A physical layer implementation encoding 1 as +5 Voltage and 0 as -5 Voltage (Source: [Brief](https://www.youtube.com/watch?v=Q3qqd6Y2FbQ&amp;ab_channel=Brief))_

  
Well, it might be `1001`. That is the case if it takes _this_ long to transmit a single bit (demonstrated by the dashed orange line in the diagram below):

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-54.png)
_An example bitstream encoded by this signal (Source: [Brief](https://www.youtube.com/watch?v=Q3qqd6Y2FbQ&amp;ab_channel=Brief))_

However, it might also represent other bit streams. For instance, if it only takes half the time to transmit a single bit (demonstrated by the dashed green line below), then the bit stream might be `11000011`:  


![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-55.png)
_Another possible bitstream encoded by the same signal (Source: [Brief](https://www.youtube.com/watch?v=Q3qqd6Y2FbQ&amp;ab_channel=Brief))_

The difference lies in the time dedicated for transmitting a single bit. This is called the **bitrate –** that is, the number of bits that are conveyed per unit of time.

Of course, achieving a high bitrate is preferable, as it means we can send many bits in a short timeframe. But it is hard to achieve high bitrates without getting many errors.

This is only one of the things that the first layer needs to take into consideration. The important thing for now is the goal of this layer: to transmit and receive a single bit.

## The Second Layer – The Data Link Layer

The second layer is responsible for transmitting data between **two hosts that are directly linked**, despite possible errors.

What do we mean by “directly linked”? For now, imagine that there is no device in between the two devices. So, if we have two computers here – computer A and computer B, and they are connected via computer M – then computer A and computer B are NOT directly linked. But computer A and computer M **are** directly linked, and so are computer M and computer B.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-56.png)
_Two remote hosts connected via another device (Source: [Brief](https://www.youtube.com/watch?v=Q3qqd6Y2FbQ&amp;ab_channel=Brief))_

Another way to put it is that computer A and computer M are **one hop** away from one another, whereas computer A and computer B are **two hops** away. 

That is, in order to get from computer A to computer B we need two “hops” – one hop from A to M, and another hop from M to B.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-57.png)
_Every direct connection is called a Hop (Source: [Brief](https://www.youtube.com/watch?v=Q3qqd6Y2FbQ&amp;ab_channel=Brief))_

Going back to the second layer's responsibility – we mentioned it is responsible for transmitting data between two hosts that are directly linked, **despite possible errors**.

What do we mean by **errors**? The physical layer might provide erroneous data. For example, `1` instead of `0`. So a stream of bits such as `000110`, might be received as `001110`. 

Many reasons might cause these kind of errors. For instance, we can think of a truck literally running over the wire where the bits are transmitted, causing some problem. Regardless of the reason, the second layer must handle the communication despite these errors.

The second layer sends data in _datagrams_, that is, in chunks. Datagrams in this layer are called **Frames**. Frames will usually contain **MAC addresses**, which are physical addresses, one identifying the sender, and another identifying the receiver.  
  
Why would we need a MAC address?

First, the receiving devices would like to know whether the frame is intended for them. The receiver wouldn’t like to waste precious time reading data intended for someone else. If the frame contains a MAC address that doesn’t belong to a receiver's device, that device can simply ignore this frame.

Second, for privacy reasons - we would like messages to arrive only at intended receivers, so only they can read the data.

Third, the sender would like the receiver to know who sent the frame. That way, the receiver will be able to send their response back to the sender, and not to someone else.

Note that we would like these addresses to be unique. That is, we want one address to identify a single device. That way, we know that if we send a message to a specific address it will be sent to the intended device only.

## The Third Layer – The Network Layer

The third layer is responsible for **routing** – that is, determining the path where the data will “travel”.

You can think of this layer as the successful routing app, Google Maps. When you get in the car and use Google Maps, you tell the app your destination, and Google Maps finds out the best route for you to drive in. 

Notice that Google Maps is dynamic – it won’t necessarily pick the same route each time. Sometimes, one path will have a traffic jam, so Google Maps will prefer another route.

We said that the second layer has physical addresses, called MAC addresses. The third layer is responsible for **logical addresses**, such as **IP addresses**.

In this layer, datagrams are called **packets**.

Consider the following network diagram:

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-59.png)
_A network diagram with Computer A in France, Computer B in the US, and 10 routers in between (Source: [Brief](https://www.youtube.com/watch?v=Q3qqd6Y2FbQ&amp;ab_channel=Brief))_

We have two computers here – one in France, and one in the United States. Of course, they are not directly linked. Rather, they are linked via third layer devices called **routers**.

Which layer is responsible for each connection?

Consider the connection between Computer A and Router 1. The second layer is responsible for this connection. What about the connection between Router 2 and Router 5? Right, again, this is the second layer. The same applies for each connection between two directly linked devices.

The third layer is responsible for defining the route – that the message sent from Computer A to Computer B will go through Routers 1, 2, 5, 8 and 10, and not in another way.

Note that there may be different implementations for each layer. For instance, we may have different implementations of the second layer. So while the connection between computer A and Router 1 might be over an Ethernet cable, the connection between Router 1 and 2 might be wireless and use WiFi. The connection between Router 2 and Router 5 might use a carrier pigeon, while the connection between router 5 and 9 will also use WiFi.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-61.png)
_The second layer may be implemented differently on every link (Source: [Brief](https://www.youtube.com/watch?v=Q3qqd6Y2FbQ&amp;ab_channel=Brief))_

The third layer does not care about these changes, but the second layer definitely does. If the carrier pigeon that transmits data from Router 2 to Router 5 is sick, the second layer will have to handle it. The data link layer will also have to make sure the data transmitted over the air between routers 1 and 5 is valid and without errors. 

## Interim Summary

So far we have covered three of the five layers.  To recap:

* The physical layer is responsible for transmitting a single bit, `1` or `0`, over the network. 
* The data link layer is responsible for transmitting data between directly linked devices, that is – devices connected via a single hop. 
* The third layer is responsible for transferring data between hosts that are connected via multiple hops. It determines the route, the path that the packets will travel.

## The Fourth Layer – The Transportation Layer

The fourth layer is an end-to-end layer. That is, it is responsible for communication from the source, all the way to the ultimate destination.

It allows **multiplexing** of multiple services. For example, one server may serve as a Web server, as well as a Mail server. When a client turns to that server, the client should be able to specify which service it would like to access. While the third layer specifies the address of the server, the transport layer identifies which **service** is relevant for the current communication.

In addition, the transport layer _may_ ensure reliability. So when this layer receives data from the upper layer, it splits it into chunks, sends them, and makes sure that all those chunks arrive correctly at the other end. 

Notice that the network layer is usually _not_ reliable. Packets may arrive in incorrect order, they can arrive with incorrect data, or even not arrive at all. A reliable transportation layer makes sure that the data is correctly received.

In this layer, datagrams are called **segments**.

Consider the following network diagram once more:

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-59.png)
_The network diagram again (Source: [Brief](https://www.youtube.com/watch?v=Q3qqd6Y2FbQ&amp;ab_channel=Brief))_

Which layer is responsible for what?

We have already said that the network layer is responsible for the route, that is, the path in which the packets travel. We also mentioned that the second layer is responsible for the transmission of the data between two, directly connected devices. For example, the link between Router 1 and Router 2.

The fourth layer views all of this network diagram as an abstract cloud. It doesn’t know the routers, and it doesn’t care about the structure of the network, or the routing. It assumes that the network can send a packet from one end to another:

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-62.png)
_The fourth layer sees the network as an abstract cloud (Source: [Brief](https://www.youtube.com/watch?v=LYH4DwydVAM&amp;ab_channel=Brief))_

The transportation layer makes sure that the endpoints can communicate over different services – for example, web and email. In addition, it might make sure that the connection is reliable. 

One example would be to acknowledge every received segment. For instance, when computer A sends a segment to computer B, computer B will send a special Acknowledgement segment, announcing that it has received the packet. 

## The Fifth Layer – The Application Layer

Last but definitely not least, we have the fifth layer, or **Application Layer.** This layer provides the service to the user’s application – web service, Voice over IP (VoIP), network games, streaming, and so on. 

According to the layers model, the fifth layer doesn’t care at all about the network. It relies on the fourth layer, as well as the lower layers, to transmit the data from one endpoint to another. The fifth layer will use this service for the various needs of the application. 

Different protocols will be used for different applications. For instance, HTTP protocol is commonly used for serving web pages on the World Wide Web. SMTP is a protocol used for emails, FTP for exchanging files, and there are many, many more.

# What is Encapsulation?

The goal of networks is to transmit data from one host to another.

To achieve this goal, each layer adds its own **header** to the data. A header contains information specific for that layer, and it precedes the data itself. 

Consider a case where we have a lookup service, used in order to find a person’s phone number, given the person's name. The data consists of the person’s first and last name. 

Before the packet is sent, the fifth layer might add its own **header**, describing that this is a REQUEST packet. The header might also specify that this is a request to map from a person’s name to a phone number, and not vice versa.  


![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-64.png)
_Header of the 5th layer, with data (Source: [Brief](https://www.youtube.com/watch?v=DBLtFjrTvD0&amp;ab_channel=Brief))_

Then, the fifth layer passes the data to the fourth layer. Note, that the fourth layer regards everything as data – ones and zeroes. It doesn’t care if the fifth layer added a header, or what is written inside that header. 

The fourth layer then adds its own header. For instance, it might specify that the requested service is the names-and-phones service. It may also include a sequential number for the packet, so it can be identified later.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-65.png)
_Header of the 4th layer, with data which includes the 5th layer's header (Source: [Brief](https://www.youtube.com/watch?v=DBLtFjrTvD0&amp;ab_channel=Brief))_

Afterwards, the fourth layer will pass the packet to the third layer. Again, the third layer will regard everything it has received – including the data itself, the header added by the fifth layer, and the header added by the fourth layer – simply as a chunk of data. 

Then, the third layer will add its own header. For instance, it may include the source address and destination address of the packet.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-66.png)
_Header of the 4th layer, with data which includes the 4th layer's header and data (Source: [Brief](https://www.youtube.com/watch?v=DBLtFjrTvD0&amp;ab_channel=Brief))_

This process goes on. So, each layer adds its own header to the packet*. This process is called **encapsulation**.

On the other end, the receiver gets the packet and needs to read and remove the headers.

* The second layer may also include a _trailer_ – an additional chunk of bits following the data, with some information.

# Putting it All Together

Now that we have covered the five layers, let’s have one example using all of them together. 

Let’s say we would like to send a video file to our friend who lives in France, while we are enjoying a trip in Argentina. For that, we are using an email service. 

The fifth layer defines how the email will be transmitted. For example, it includes the email address of the sender, as well as the receiver. It contains a title, and the body of the message. It requires that we follow a specific template of an email address, that will be included in the header of this layer. 

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-63.png)
_The five layers model, with an example of sending an email (Source: [Brief](https://www.youtube.com/watch?v=LYH4DwydVAM&amp;ab_channel=Brief))_

Then, the fifth layer uses the fourth layer in order to split the email into chunks. Of course, each chunk will also carry the fourth layer's header. It is also used in order to specify that we are currently using an email service. 

In this case, we definitely want the connection to be reliable – so the receiver will be able to play our video file correctly. Thus, the fourth layer will also handle reliability. On the receiver’s end, it might send an acknowledgment packet for every packet it receives.

The third layer will define the best route for every packet to be sent. It might choose different routes for different packets. Among other things, its header will contain the source and destination addresses for the packet.

The second layer will be responsible for every link between two directly connected devices. Its header will include the MAC addresses for each device. 

The first layer is responsible for encoding all the ones and zeros, and to pass them over the line. And then, decoding and reading those ones and zeroes on the other end. On this layer, we don't really have a header, as it consists of single bits only.

This way, every layer uses the services provided by the lower layers, and the huge problem of transmitting data over the network becomes doable. How amazing is that?

# Summary

In this post you learned what the five layers model is and why we need layers. You should now understand what each layer is responsible for, and you can fit every topic you encounter in Computer Networks into this model.

## About the Author

[Omer Rosenbaum](https://www.linkedin.com/in/omer-rosenbaum-034a08b9/) is [Swimm](https://swimm.io/)’s Chief Technology Officer. He's the author of the Brief [YouTube Channel](https://youtube.com/@BriefVid). He's also a cyber training expert and founder of Checkpoint Security Academy. He's the author of [Computer Networks (in Hebrew)](https://data.cyber.org.il/networks/networks.pdf). You can find him on [Twitter](https://twitter.com/Omer_Ros).

### Additional References

* [Computer Networks Playlist - on my Brief channel](https://www.youtube.com/playlist?list=PL9lx0DXCC4BMS7dB7vsrKI5wzFyVIk2Kg).
* [The Seven Layer model explained in plain English](https://www.freecodecamp.org/news/osi-model-networking-layers-explained-in-plain-english/)
* [The TCP/IP model – layers and protocol explained](https://www.freecodecamp.org/news/what-is-tcp-ip-layers-and-protocols-explained/)

