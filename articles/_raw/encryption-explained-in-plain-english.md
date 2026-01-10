---
title: Symmetric and Asymmetric Key Encryption – Explained in Plain English
subtitle: ''
author: Daniel Adetunji
co_authors: []
series: null
date: '2023-04-05T20:09:48.000Z'
originalURL: https://freecodecamp.org/news/encryption-explained-in-plain-english
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/cover.jpg
tags:
- name: encryption
  slug: encryption
- name: information security
  slug: information-security
seo_title: null
seo_desc: 'Encryption is a way of scrambling data so that it can only be read by the
  intended recipient.

  Encryption is an integral part of our daily lives – whether you are sending messages
  to friends on WhatsApp, visiting a website and your browser is making s...'
---

Encryption is a way of scrambling data so that it can only be read by the intended recipient.

Encryption is an integral part of our daily lives – whether you are sending messages to friends on WhatsApp, visiting a website and your browser is making sure it's legitimate, or entering your bank details when buying something online. Encryption protects your data from potentially malicious and prying eyes.

This article will cover:

* Encryption algorithms and keys
    
* Symmetric and asymmetric key encryption
    
* How TLS/SSL uses both symmetric and asymmetric encryption
    

## Encryption Algorithms and Keys

At the start of this article, I described encryption as a way of scrambling data so that it can only be read by the intended recipient. Let’s break down what this means.

Let's say you want to write a letter to your friend and want to ensure that only the friend can read its contents. How would you prevent the prying eyes of all the intermediaries the letter could pass through before it gets to your friend? That is, how do you prevent the postman, the concierge in their building, or one of their friends from reading the letter?

You start with an unscrambled letter that anyone can read. This is called **plaintext**. To scramble the contents of the message, you need an **encryption algorithm** and a **key**. The encryption algorithm uses the key to scramble the contents of the message. This encrypted message is called **ciphertext**.

The process of encryption is shown in the image below:

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-9.png align="left")

When your friend gets the message, they will need to descramble it using the **algorithm** and the **key**. This is illustrated below:

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-10.png align="left")

The two key ingredients needed to send a message to your friend that only they can read is an **encryption algorithm** and a **key**.

The encryption algorithm is simply a mathematical formula designed to scramble data, while the key is used as part of the formula. The encryption algorithm is generic, but the key, used as an input to the algorithm, is what ensures the uniqueness of the scrambled data.

Let’s look at one of the simplest encryption algorithms, called the Caesar Cipher. In its simplest form, this algorithm simply replaces each letter by the next letter in the alphabet. So A becomes B, and B becomes C and so on.

With this algorithm, the text ‘Birthday Surprise’ becomes ‘Cjsuiebz Tvsqsjtf’, indistinguishable from gibberish to the untrained eye.

With the Caesar Cipher example, the **algorithm** is the formula used to replace each letter of the alphabet with another. The **key** is the number of shifts made between each letter. With a key of 0, A is A, an obviously poor choice of key as the data is unscrambled. With a key of 1, A becomes B. With a key of 10, A becomes K.

The Caesar Cipher is a relatively poor encryption algorithm. Why? Since there are only 26 letters in the English language, you can only produce a maximum of 25 possible ciphertexts. If you don’t have the key, you only need to shift each letter up to 25 times until you see coherent words and sentences, at which point you know that you have successfully decrypted the message.

A bad encryption algorithm is one that is easily decrypted by using a small amount of brute force (that is, trying every possible permutation) – and 25 possible ciphertexts is an objectively small number of possible options to go through.

Modern encryption algorithms like AES-256 used by AWS, GCP, and Azure for encrypting data are considerably more complicated and secure than the Caesar Cipher. Based on current computing capability, it would take trillions and trillions of years for the most advanced supercomputer to use brute force to decrypt data encrypted using AES-256 \[[1](https://scrambox.com/article/brute-force-aes/)\]. Even the universe is not that old.

## Symmetric and Asymmetric Key Encryption

The core of any encryption process is the encryption algorithm and the key. There are many types of encryption algorithms. But there are, broadly speaking, two types of keys – symmetric and asymmetric keys.

In symmetric key encryption, the same key used to encrypt the data is used to decrypt the data. In asymmetric key encryption, one key is used to only encrypt the data (the public key) and another key is used to decrypt (the private key).

### Asymmetric key encryption

First, let’s look at asymmetric key encryption with a simple analogy.

Imagine you wanted to send something to your friend, but it was absolutely essential that nobody else, except your friend, could have access to that object. So, your friend buys an indestructible box, fabricated from the strongest metal on the planet, and sends it to you so that you can place the object in it. Your friend also sends you the key that can only be used to lock the box.

Now, this box has one more special property. It has two keyholes. One keyhole to open the box, another to lock the box.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-11.png align="left")

Naturally, this box will also need two keys – one to open and another to lock it.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-12.png align="left")

Both keys are similar, but not identical. As you can see in the image above, for example, the key used to open the box has two prongs while the key used to lock the box has three prongs.

As the sender of the object, all you have is the box to place the object in and a key to lock the box. Only your friend has the key that can unlock the box.

The key used to lock the box is called the public key, and cannot be used to open it, as that requires the private key. If anyone intercepted the package and made a copy of the public key, it could not be used to open the box, only to lock it. Only the person who holds the private key can open the box.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-13.png align="left")

Asymmetric key encryption is used when there are two or more parties involved in the transfer of data. This type of encryption is used for encrypting data in transit, that is encrypting data being sent between two or more systems. The most popular example of asymmetric key encryption is [RSA](https://nordvpn.com/blog/rsa-encryption/).

### Symmetric key encryption

Symmetric key encryption uses the same key for encryption and decryption. This makes sharing the key difficult, as anyone who intercepts the message and sees the key can then decrypt your data.

This is why symmetric key encryption is generally used for encrypting data at rest. AES-256 is the most popular symmetric key encryption algorithm. It is used by AWS for encrypting data stored in hard disks (EBS volumes) and S3 buckets. GCP and Azure also use it for encrypting data at rest.

## How TLS/SSL Uses Both Symmetric and Asymmetric Encryption

The main strength of symmetric key encryption is that it is computationally easier and faster to encrypt and decrypt data using a single key, just as it is easier to build a box with a single lock and key.

The weakness of symmetric key encryption is that if the key is exposed, your data is no longer securely encrypted. So, if you needed to share the key with an external party, there is a risk that the key could be exposed, leaving your data at risk of being decrypted.

Symmetric key encryption is ideal for encrypting data at rest, where you do not need to share the key with another system.

With asymmetric encryption, this is not a problem since two separate keys are used – the public key to encrypt data and the private key to decrypt data.

The public key can be easily shared with anyone and poses no risk to your data being decrypted, since the private key is needed for decryption.

The drawback of asymmetric key encryption is that the encryption and decryption process is slower and more complicated. Asymmetric key encryption is ideal for encrypting data in transit, where you need to share the key with another system.

What if there was a way of getting the speed and computational simplicity of symmetric encryption without increasing the risk of exposing your keys?

TLS/SSL encryption use both symmetric and asymmetric keys to encrypt data in transit, and is used with the HTTP protocol for secure communications over a computer network.

### TLS/SSL Encryption Explained

TSL (Transport Layer Security) and SSL (Secure Sockets Layer) are often used interchangeably to mean the same thing. But when people say SSL, they often mean TLS.

TLS is generally considered more secure than SSL due to several improvements made to the protocol, such as stronger cryptographic algorithms. Due to security concerns with SSL, most modern web browsers and applications have dropped support for SSL and only support TLS. As a result, TLS has become the standard for secure communication over the internet.

### How to Use Symmetric and Asymmetric Encryption at the Same Time

Let's say you want to securely send a parcel to your friend. But you don’t want to keep using the special indestructible box that has two keyholes and two locks. It is expensive, heavy and impractical to use for frequent communications. You still want to use an indestructible box, but one that is simpler, with a single lock and key.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-14.png align="left")

However, if you are using a box with only a single lock and key, you now need to figure out how to securely share the key for that simpler box with your friend.

Since the same key is used to both open and lock it, you cant just send the key to your friend without somehow protecting it first. If the key is intercepted and a copy is taken by someone, they can now open your box and take what is inside.

How can you securely share this key with your friend so that you can use this simpler box for future communication?

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-15.png align="left")

1. First, your friend sends the box with the two locks plus the public key used to lock it. But you don’t want to keep using this box. You will only use this box once – to transfer the key for another simpler box that you will use for future exchanges.
    
2. You place the master key that will be used in future exchanges inside this box and lock it with the public key sent by your friend.
    
3. You send the locked box which contains a copy of the master key inside back to your friend.
    
4. Your friend uses his private key to open the box. Now you both have the master key and can be sure no one else has it since it was sent in a secure box
    
5. All future items are then placed in this simpler box with a single lock and key which can be opened and locked using the master key you just sent to your friend.
    

### TLS/SSL Encryption Sequence

The analogy in the previous section neatly maps to how TLS/SSL encryption actually works. But there are some prerequisite steps which I ignored in this analogy, like creating a TCP connection and the server sending its certificate (Steps 1 and 2 below).

Also, Step 6 is a simplification of the process. In reality, the master key is used to generate a further set of keys that the client and server will use to encrypt and decrypt messages and also to authenticate that the messages were indeed sent by the client and server.

To read more about the low level detail, I’d recommend Chapter 8 of "[Computer Networking](https://www.amazon.co.uk/Computer-Networking-Global-James-Kurose/dp/1292405465/ref=sr_1_1?keywords=computer+networking+a+top-down+approach&qid=1680219419&sprefix=computer+netw%2Caps%2C168&sr=8-1)" by Kurose & Ross.

But, at a high level, the sequence is as follows:

1. Client establishes TCP connection with the server
    
2. Client verifies that the server is who it says it is – server sends certificate which has the public key. The accompanying private key remains with the server.
    
3. Client creates a master secret key and uses the server's public key to encrypt it. This master secret key is a symmetric key so the same key is used for encryption and decryption.
    
4. Client sends the encrypted master secret key to the server.
    
5. Server decrypts the encrypted master key using its private key.
    
6. All future messages between client and server now use the symmetric master key to encrypt and decrypt messages.
    

## Best of Both Worlds

Using both symmetric and asymmetric key encryption gives you the speed of symmetric key encryption without compromising on the extra security provided by asymmetric key encryption.

But nothing comes for free, of course. With TLS, there is an added layer of complexity since you need to first use asymmetric keys to establish a secure connection before exchanging the symmetric key for future communication.

So by using both symmetric and asymmetric encryption, TLS/SSL gets the best of both worlds with limited downsides.
