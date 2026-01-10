---
title: How to Send Secret Messages
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-08T21:04:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-send-secret-messages
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca196740569d1a4ca4f7c.jpg
tags:
- name: Cryptography
  slug: cryptography
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Megan Kaczanowski

  Cryptography is the science of using codes and ciphers to protect messages, at its
  most basic level. Encryption is encoding messages with the intent of only allowing
  the intended recipient to understand the meaning of the message...'
---

By Megan Kaczanowski

Cryptography is the science of using codes and ciphers to protect messages, at its most basic level. Encryption is encoding messages with the intent of only allowing the intended recipient to understand the meaning of the message. It is a two way function (you need to be able to undo whatever scrambling you’ve done to the message). This is designed to protect data in transit. 

One of the earliest ciphers involved a simple shift. For example, if you just shift all the letters in the alphabet by a few, the alphabet might look like the following:

ABCDEFGHIJKLMNOPQRSTUVWXYZ

NOPQRSTUVWXYZABCDEFGHIJKLM

Then, each letter of the alphabet corresponds to a different letter, but it is difficult to figure out which one, if you don’t already know. Using this cipher, the message, ‘Hello’ translates to ‘Uryyb’.

Unfortunately, advances in analysis, particularly pattern analysis driven by very powerful computers, made these types of cyphers very easy to break. 

In response to that, we’ve developed very strong, complex algorithms. These can be broken down into two basic types of encryptions — symmetric algorithms and asymmetric algorithms. 

Symmetric algorithms are also known as ‘secret key’ algorithms, and asymmetric algorithms are known as ‘public key’ algorithms. The key difference between the two is that symmetric algorithms use the same key to encode and decode (see the first figure below), while asymmetric algorithms use different keys for encryption and decryption (see the second figure below).

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screen-Shot-2019-06-13-at-4.56.58-PM.png)

As you can see in the above figure, with symmetric encryption, if Bob and Midge want to communicate, Bob first encrypts his message with the secret key (the encrypted message is called ciphertext). Then he sends it to Midge. Midge then decrypts the message with the same secret key and is able to read the message. To send a message back, the process is reversed. 

This process is fast, scalable, and very secure. The problem with it is that it requires both parties to already have the same secret key. If they don’t, they need to pass it along insecure channels, which essentially removes the security of the encryption.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screen-Shot-2019-06-13-at-4.57.02-PM.png)

With Asymmetric encryption, as in the above figure, if Bob and Midge want to communicate, Bob encrypts his message with Midge’s public key and sends it to her. She then decrypts the message with her private key to read it. To send a message back, the process is reversed. 

In this way, anyone can send Midge a message, as she can make her public key available to anyone, but only she can decrypt a message (as she keeps her private key secret). It also solves the need to pass a secret key along insecure channels, because there is no need to pass a secret at all. The disadvantage is that it requires everyone who wants to communicate to have two different keys (not scalable), and it is relatively slow.

In general, when talking about encryption, the most important considerations are:

* Authentication/Nonrepudiation — Whether or not you can prove where messages originated (Am I sure who sent this message?).
* Reuse — Can I continue to use this key or will it need to be regenerated for each new communication?
* Effectiveness — How fast can I transfer large amounts of data?
* Scalability — Is this feasible for large groups?
* Distribution — how do you distribute keys to the people who you’re communicating with, without divulging the secret to anyone else?

That’s where significant differences start to come up between symmetric and asymmetric encryption, summarized below:

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screen-Shot-2019-06-13-at-4.57.55-PM.png)

In order to use the best of both worlds, many modern encryption protocols will use asymmetric encryption to establish a connection and create a shared secret. Then, they will switch to symmetric encryption to benefit from the speed difference. 

%[https://twitter.com/preinheimer/status/841273046317060105]


