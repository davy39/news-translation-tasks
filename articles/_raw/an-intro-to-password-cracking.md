---
title: How to Crack Passwords
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-28T05:52:00.000Z'
originalURL: https://freecodecamp.org/news/an-intro-to-password-cracking
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c61740569d1a4ca31d0.jpg
tags:
- name: cyber
  slug: cyber-2
- name: cybersecurity
  slug: cybersecurity
- name: fintech
  slug: fintech
- name: information security
  slug: information-security
- name: passwords
  slug: passwords
seo_title: null
seo_desc: "By Megan Kaczanowski\nA brief note - this article is about the theory of\
  \ how to crack passwords. Understanding how cybercriminals execute attacks is extremely\
  \ important for understanding how to secure systems against those types of attacks.\
  \ \nAttemptin..."
---

By Megan Kaczanowski

A brief note - this article is about the theory of how to crack passwords. Understanding how cybercriminals execute attacks is extremely important for understanding how to secure systems against those types of attacks. 

Attempting to hack a system you do not own is likely illegal in your jurisdiction (plus hacking your own systems may [and often does] violate any warranty for that product). 

## Let's start with the basics. What is a brute force attack?

This type of attack involves repeatedly trying to login as a user by trying every possible letter, number, and character combination (using automated tools). 

This can be done either online (so in real-time, by continually trying different username/password combinations on accounts like social media or banking sites) or offline (for example if you've obtained a set of hashed passwords and are trying to crack them offline). 

Offline isn't always possible (it can be difficult to obtain a set of hashed passwords), but it is much less noisy. This is because a security team will probably notice many, many failed login accounts from the same account, but if you can crack the password offline, you won't have a record of failed login attempts.

This is relatively easy with a short password. It becomes exponentially more difficult with a longer password because of the sheer number of possibilities. 

For example, if you know that someone is using a 5 character long password, composed only of lowercase letters, the total number of possible passwords is 26^5 (26 possible letters to choose from for the first letter, 26 possible choices for the second letter, etc.), or 11,881,376 possible combinations. 

But if someone is using an 11 character password, only of lowercase letters, the total number of possible passwords is 26 ^11, or 3,670,344,486,987,776 possible passwords. 

When you add in uppercase letters, special characters, and numbers, this gets even more difficult and time consuming to crack. The more possible passwords there are, the harder it is for someone to successfully login with a brute force attack.

### How to protect yourself

This type of attack can be defended against in a couple of different ways. First, you can use sufficiently long, complex passwords (at least 15 characters). You can also use unique passwords for each account (use a password manager!) to reduce the danger from data breaches.

A security team can lock out an account after a certain number of failed login attempts. They can also force a secondary method of verification like Captcha, or use 2 factor authentication (2FA) which requires a second code (SMS or email, app-based, or hardware key based).

[Here's](https://null-byte.wonderhowto.com/how-to/gain-ssh-access-servers-by-brute-forcing-credentials-0194263/) an article on how to execute a brute force attack.

## How can you crack passwords faster?

A dictionary attack involves trying to repeatedly login by trying a number of combinations included in a precompiled 'dictionary', or list of combinations. 

This is usually faster than a brute force attack because the combinations of letters and numbers have already been computed, saving you time and computing power. 

But if the password is sufficiently complex (for example 1098324ukjbfnsdfsnej) and doesn't appear in the 'dictionary' (the precompiled list of combinations you're working from), the attack won't work. 

It is frequently successful because, often when people choose passwords, they choose common words or variations on those words (for example, 'password' or 'p@SSword'). 

A hacker might also use this type of attack when they know or guess a part of the password (for example, a dog's name, children's birthdays, or an anniversary - information a hacker can find on social media pages or other open source resources). 

Similar protection measures to those described above against brute force attacks can prevent these types of attacks from being successful.

## What if you already have a list of hashed passwords? 

Passwords are stored in the /etc/shadow file for Linux and C:\Windows\System32\config file for Windows (which are not available while the operating system is booted up). 

If you've managed to get this file, or if you've obtained a password hash in a different way such as sniffing traffic on the network, you can try 'offline' password cracking. 

Whereas the attacks above require trying repeatedly to login, if you have a list of hashed passwords, you can try cracking them on your machine, without setting off alerts generated by repeated failed login attempts. Then you only try logging in once, after you've successfully cracked the password (and therefore there's no failed login attempt). 

You can use brute force attacks or dictionary attacks against the hash files, and may be successful depending on how strong the hash is.

### Wait a minute - what's hashing?

35D4FFEF6EF231D998C6046764BB935D

Recognize this message? It says 'Hi my name is megan'

7DBDA24A2D10DAF98F23B95CFAF1D3AB

This one is the first paragraph of this article. Yes, it looks like nonsense, but it's actually a 'hash'. 

A hash function allows a computer to input a string (some combination of letters, numbers, and symbols), take that string, mix it up, and output a fixed length string. That's why both strings above are of the same length, even though the strings' inputs were very different lengths. 

Hashes can be created from nearly any digital content. Basically all digital content can be reduced to binary, or a series of 0s and 1s. Therefore, all digital content (images, documents, etc.) can be hashed. 

There are many different hashing functions, some of which are more secure than others. The hashes above were generated with MD5 (MD stands for "Message Digest"). Different functions also differ in the length of hash they produce. 

The same content in the same hash function will always produce the same hash. However, even a small change will alter the hash entirely. For example, 

2FF5E24F6735B7564CAE7020B41C80F1

Is the hash for 'Hi my name is Megan' Just capitalizing the M in Megan completely changed the hash from above.

Hashes are also one-way functions (meaning they can't be reversed). This means that hashes (unique and one-way) can be used as a type of digital fingerprint for content. 

### What's an example of how hashes are used?

Hashes can be used as verification that a message hasn't been changed. 

When you send an email, for example, you can hash the entire email and send the hash as well. Then the recipient can run the received message through the same hash function to check if the message has been tampered with in transit. If the two hashes match, the message hasn’t been altered. If they don’t match, the message has been changed. 

Also, passwords are usually hashed when they're stored. When a user enters their password, the computer computes the hash value and compares it to the stored hash value. This way the computer doesn’t store passwords in plaintext (so some nosy hacker can't steal them!).

If someone is able to steal the password file, the data is useless because the function can’t be reversed (though there are ways, like rainbow tables, to figure out what plaintext creates the known hash).

### What's the problem with hashes?

If a hash can take data of any length or content, there are unlimited possibilities for data which can be hashed. 

Since a hash converts this text into a fixed length content (for example, 32 characters), there are a finite number of combinations for a hash. It is a very very large number of possibilities, but not an infinite one.

Eventually two different sets of data will yield the same hash value. This is called a collision. 

If you have one hash and you're trying to go through every single possible plaintext value to find the plaintext which matches your hash, it will be a very long, very difficult process. 

### However, what if you don't care which two hashes collide?

This is called the '[birthday problem](https://en.wikipedia.org/wiki/Birthday_problem)' in mathematics. In a class of 23 students, the likelihood of someone having a birthday on a specific day is around 7%, but the probability that any two people share the same birthday is around 50%. 

The same type of analysis can be applied to hash functions in order to find any two hashes which match (instead of a specific hash which matches the other). 

To avoid this, you can use longer hash functions such as SHA3, where the possibility of collisions is lower.

You can try generating your own hash functions for SHA3 [here](https://www.browserling.com/tools/sha3-hash) and MD5 [here](http://onlinemd5.com/).  

You can try to brute force hashes, but it takes a very long time. The faster way to do that, is to use pre-computed [rainbow tables](https://www.freecodecamp.org/news/p/ee82d358-9d43-49a8-84a6-8ffca9a3ee1f/www.freecodecamp.org/news/why-a-little-salt-can-be-great-for-your-passwords) (which are similar to dictionary attacks).

## It seems really easy to get hacked. Should I be concerned? 

The most important thing to remember about hacking is that no one wants to do more work than they have to do. For example, brute forcing hashes can be extremely time consuming and difficult. If there's an easier way to get your password, that's probably what a nefarious actor will try first. 

That means that enabling basic cyber security best practices is probably the easiest way to prevent getting hacked. In fact, Microsoft [recently reported](https://www.zdnet.com/article/microsoft-using-multi-factor-authentication-blocks-99-9-of-account-hacks/) that just enabling 2FA will end up blocking 99.9% of automated attacks. 

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Shot-2019-08-27-at-1.18.47-PM.png)
_[https://xkcd.com/538/](https://xkcd.com/538/)_

**Additional Reading:**

[Popular password cracking tools](https://resources.infosecinstitute.com/10-popular-password-cracking-tools/#gref)

