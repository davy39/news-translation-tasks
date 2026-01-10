---
title: How your phone opens medium.com — I’ll let a doorman and a librarian explain.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-25T12:29:40.000Z'
originalURL: https://freecodecamp.org/news/how-can-your-phone-open-medium-com-62ec36b1429f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*53k-kW_pi3-Ai382HAH8Ow.jpeg
tags:
- name: internet
  slug: internet
- name: mobile
  slug: mobile
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Andrea Zanin

  Hey did you notice what just happened? You clicked a link, and now here you are
  reading this article. But did you think about how your browser knew that the link
  you clicked referred to this article, and that this article contained th...'
---

By Andrea Zanin

Hey did you notice what just happened? You clicked a link, and now here you are reading this article. But did you think about how your browser knew that the link you clicked referred to this article, and that this article contained these words?

It’s something so common that we forget about it, but the mechanism behind it is fascinating. In this article we will explore it using real world analogies.

### How computers talk

When you open a website, your browser is asking some other computer somewhere in the world for the data that will allow it to show you the page (for example, the text you are reading now).

This act of asking another computer is not unlike sending a piece of mail (physical mail, not an email) to a friend and waiting for his reply.

If John wants to send Brittany some mail, he needs to know her address. In the internet world, instead of having physical addresses we have IP addresses. They work the same way, just with a computer instead of a mailbox.

### Tell me more about this IP thing

Before we dive in the details about IP addresses, I want you to imagine that you are staying in a luxurious hotel with hundreds of rooms and a fancy doorman (not bad right?).

Now back to IP addresses: your standard IP address looks like this: 102.134.122.234. The first 9 digits are the address of the virtual hotel you are staying in, while the last 3 are your room. While the address of the virtual hotel is fixed, the room you are staying in is chosen by the hotel.

If anyone wants to send you a message, they need to know the address of the hotel and your room number. So they send the message to the hotel and the doorman delivers it directly to you.

The virtual hotel is like your home WiFi network. Its address is decided by your internet provider, while your room number is decided by your home router.

### Numbers are complicated

You may have noticed that if you want to open medium.com you don’t need to know its IP address. This is where the internet becomes smarter than the postal service.

On top of IP addresses, there is a system to match easy to remember names to IPs: the Domain Name System.

Finally, here is what happens when your phone wants to open medium.com

* The phone sends the request to the doorman (router) and asks it to send it to medium.com
* the router asks a trusted agency (your internet provider) for the IP of medium.com
* this trusted agency then refers to a worldwide organization (the Root Server) that recognizes the Top Level Domain (.com, .us, .org, …)
* the Root Server then asks the digital librarian responsible for that TLD
* finally the librarian opens his master record, looks for the website we requested, and responds with the IP

![Image](https://cdn-media-1.freecodecamp.org/images/9WfzmmiTuw5U2o4YwfFGfM4U2frg8OXY4k08)

Finally your phone can send the request directly to Medium’s address (IP). All of this in less than a tenth of a second.

### Will we run out of addresses?

Yes we will run out of IP addresses — and soon. But don’t panic, a solution is already being implemented.

First we have to take a step back: up until now I talked about IP addresses, but I should have said IP version 4. The solution is IP version 6, and it looks even uglier: 2001:0db8:0000:0042:0000:8a2e:0370:7334

This alphanumeric monstrosity leads to an astronomical amount of possible IPs, so issue solved ??.

### Before you leave

In this article we analyzed how your phone understands what medium.com is, but what about the HTTPS part of the link? I wrote another article about it: [https explained with carrier pigeons](https://medium.freecodecamp.org/https-explained-with-carrier-pigeons-7029d2193351).

If you liked the article don’t forget that you can ? up to 50 times.

