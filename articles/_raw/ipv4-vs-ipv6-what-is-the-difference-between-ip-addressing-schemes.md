---
title: IPV4 vs IPV6 – What is the Difference Between IP Addressing Schemes?
subtitle: ''
author: Dionysia Lemonaki
co_authors: []
series: null
date: '2021-10-15T16:30:13.000Z'
originalURL: https://freecodecamp.org/news/ipv4-vs-ipv6-what-is-the-difference-between-ip-addressing-schemes
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/nasa-1lfI7wkGWZ4-unsplash.jpg
tags:
- name: computer network
  slug: computer-network
- name: computer networking
  slug: computer-networking
- name: internet
  slug: internet
- name: ipv6
  slug: ipv6
seo_title: null
seo_desc: 'The Internet is one of our greatest inventions.

  Millions of people use the Internet every second of the day, and it has changed
  many aspects of our lives – from creating new jobs and a new way of working to influencing
  how news is consumed and how de...'
---

The Internet is one of our greatest inventions.

Millions of people use the Internet every second of the day, and it has changed many aspects of our lives – from creating new jobs and a new way of working to influencing how news is consumed and how decisions are made.

Although it's been around for quite a while now, the underlying technologies that power it have not changed that much since its invention.

In this article you'll learn about the Internet Protocol, or IP - what it is, how it works, and the differences between its different versions. 

## How computers communicate over the Internet

Computers, and devices in general, connect and communicate with one another on the Internet in a couple different ways: either with the help of a large number of undersea cables or wirelessly.

Information gets broken down into packets, or smaller pieces of data, that get transferred by routers to the correct destination and back.

However, for computers to communicate in the first place, there needs to be a set and universally agreed upon common language of communication that all devices understand.

This need for a standardized method of communication during data exchange led to the creation of protocols.

One of the key protocols is the *Internet Protocol*, or IP.

The Internet Protocol has a particular syntax that defines a set of rules and a specified format for how communication will take place between devices over various networks. It essentially makes communication between computers possible.

Those rules cover a large number of things, like:
* identifying and locating each device on a network
* having devices then talk to each other
* dictating how the format and transfer of packets of data will look like
* determining how each packet will reach the desired destination
* choosing the fastest and most efficient path possible for the router to take, and
* deciding how to handle errors when they occur.

Each and every device connected to a network needs a way to identify itself across various networks.

When you want to send a letter to someone, you need a way of identifying that person's home so the postal service knows where to deliver the letter. You don't want the letter to be delivered to the wrong person! 

This is why, when sending a letter, you include the recipient's unique home address as the destination address and also your unique home address, which is the return address. 

Each house has a unique address that sets it apart and identifies it.

Similarly, the way to identify computers and devices on the Internet so we can transmit and exchange data, is by knowing their IP address. 

To send an e-mail to someone, you need to know their computer's IP address. The e-mail gets broken down into smaller chunks, or packets. The way they  reach the correct destination is because each packet also includes IP information. 

When sending something over the Internet there needs to be a destination address and a return address on each packet. IP addresses are how computers find one another and know their respective locations.

The Internet Protocol is in charge of defining the format of IP addressing.

## What is an IP address?

An IP address is a network address, and every device that connects to a computer network gets one.

An IP address is a unique sequence of numbers assigned to a device that's written in a certain format. It globally identifies every device in the interconnected network.

As mentioned earlier, packets get routed to the correct and intended destination and devices are able to send and receive information over the Internet because each device is assigned a unique IP address.

You'll likely not ever have to deal directly with IP addresses or know any by heart in order to send information over the Internet - it's all happening behind the scenes.

If you're curious and want to know your IP address, head to Google.com and type in "What's my IP" and you'll see your unique address in the first result.

That being said, there are are few different types of IP addresses, which you'll see in the following sections.

### Private vs Public IP addresses

Everyone has two kinds of IP addresses: public and private.

The public one is given to your home router by your Internet Service Provider (ISP) and it's the primary address for your whole local network.

In your home you may have more than one laptop, smartphone, or tablet. Each device has its own IP address, but they are all also under the same main, public IP address. 

This is how all devices in your home get connected to the Internet – via the main public IP address. 

A public IP address is unique, meaning there are no two identical IP addresses used at a given moment.

As mentioned above, if you have many devices in your home, then each has its own IP address. This address is a private IP address, and it cannot access the Internet directly.

As these devices connect to the Internet via the router (which has a public IP address), the router needs a way to identify and recognise each device separately, before it connects it to the Internet.

The way the router does this is by assigning an individual private IP address to each device. Then it remembers that address each time the device wants to get connected to the Internet.

### Dynamic VS Static IP Addresses

Public IP addresses are split into two categories: dynamic and static.

Once a device gets connected to the Internet, your Internet Service Provider gives you one of their available IP addreses for the duration of the time you stay connected. This is how the device will be able to send and receive data.

The next time you connect to the Internet, your ISP will provide you with a *different* IP address. This means that each time you connect to the Internet, you have a different IP address. This is why this type of IP address is called dynamic - it's ever changing.

On the other hand, a static IP address never changes. It's a permanent address. The address is provided once and you can expect it to stay the same.

Static IP addresses are often used by DNS Servers. A DNS server is a large computer that stores files that make up a website. Their job is to send those files each time they are requested by a user who wants to view the website.

## IPv4 vs IPv6 – What's the Difference? 
### What is an IPv4 address?

IPv4 is the first, and most widely used, version of the Internet Protocol.

It was first launched in  1980 and is used to this day.

It's a 32-bit address and it's made up of 4 blocks – with each block being separated by a dot. 

It looks something like this:

```
XXX.XXX.XXX.XXX
```

Each block can fit up to 3 digits, and the numbers in the block range from 0 to 255, in *decimal* values.

An example of an IP address is:

```
142.250.185.206
```

Here's another example:

```
69.171.250.35
```

These decimal numbers are converted to binary, a machine language, which is the only language computers can directly understand. 

These decimal numbers, in binary, are actually 4 blocks of 8 binary digits (or bits).

This is why it is called a 32-bit address – it's an address made up of a sequence of 32 binary digits. 

For example, the address you saw earlier,`142.250.185.206` is:

```
10001110.11111010.10111001.11001110
```

in binary, under the hood.

So, `2^32` is a total of 4,294,967,296 unique addresses. That is the limit  of IP addresses IPv4 can provide for each device to connect to the Internet.

You would think that this large number is more than enough. But, as the population continues to grow and each person owns more and more devices (and each device needs its own IP address) we have been running out of addresses for quite some time now.

### What is IPv6?

IPv6 is the latest version of the Internet Protocol which was first deployed in 1998.

It's the successor of IPv4 and there will be a slow shift towards it in the future.

Whereas IPv4 is a numeric address, IPv6 uses hexadecimal, alphanumeric characters - meaning it contains numbers *and* letters.

In the way IPv4 uses 4 blocks that each contain up to 3 digits, IPv6 uses 8 blocks that contain 4 hexadecimal characters each.

In IPv4, each block is separated by a do t(`.`). In IPv6 each block is separated by a colon (`:`).

So, an IPv6 address looks something like this:

```
XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX:XXXX
```

For example:

```
2001:0db8:85a3:0000:0000:8a2e:0370:7334
```

It's a 128-bit address, meaning that there are `2^128` addresses available.

That means there are 340,282,366,920,938,463,463,374,607,431,768,211,456 addresses we can use on the Internet. 

That is 340 *undecillion* addresses, which we hope will be more than enough for everyone!

## Conclusion

And there you have it! You now know the basics of the Internet Protocol. It's the underlying technology all computers and devices use to be able to connect with one another and receive and exchange information.

You also learned the basic differences between IPv4 and IPv6. And in a nutshell, IPv6 provides far more IP addresses than IPv4 does.

If you are interested in learning more about how the Internet works, check out this [video on freeCodeCamp's YouTube channel](https://www.youtube.com/watch?v=zN8YNNHcaZc&t=1s) that explains the fundamentals of computer networking.

Thanks for reading and happy learning 😊



