---
title: Encryption Algorithms Explained with Examples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-01T00:16:00.000Z'
originalURL: https://freecodecamp.org/news/understanding-encryption-algorithms
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b58740569d1a4ca2b3f.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: encryption
  slug: encryption
- name: Ethical Hacking
  slug: ethical-hacking
- name: hacking
  slug: hacking
- name: technology
  slug: technology
seo_title: null
seo_desc: "By Megan Kaczanowski\nCryptography, at its most basic, is the science of\
  \ using codes and ciphers to protect messages. \nEncryption is encoding messages\
  \ with the intent of only allowing the intended recipient to understand the meaning\
  \ of the message. It..."
---

By Megan Kaczanowski

Cryptography, at its most basic, is the science of using codes and ciphers to protect messages. 

Encryption is encoding messages with the intent of only allowing the intended recipient to understand the meaning of the message. It is a two way function (you need to be able to undo whatever scrambling you’ve done to the message). This is designed to protect data in transit. 

If you're looking for a general background on the difference between symmetric and asymmetric algorithms and a general overview of what encryption is, start [here](https://medium.com/swlh/how-to-send-secret-messages-1c106250b884). This article will primarily cover two of the most commonly used encryption algorithms. 

As a general overview, there was a major problem with symmetric algorithms when they were first created - they only functioned effectively if both parties already knew the shared secret. If they didn't, securely exchanging a key without a third party eves-dropping was extremely difficult. 

And if a third party obtained the key, it was very easy for them to then break the encryption, defeating the purpose of secure communication. 

Diffie-Hellman solved this problem by allowing strangers to exchange information over public channels which can be used to form a shared key. A shared key is difficult to crack, even if all communications are monitored.

## How does Diffie-Hellman work?

Diffie-Hellman is what's called a key exchange protocol. This is the primary use for Diffie-Hellman, though it could be used for encryption as well (it typically isn't, because it's more efficient to use D-H to exchange keys, then switch to a (significantly faster) symmetric encryption for data transmission). 

The way this works is as follows:

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screen-Shot-2019-10-04-at-5.45.13-PM.png)
_[https://en.wikipedia.org/wiki/Diffie–Hellman_key_exchange#/media/File:Diffie-Hellman_Key_Exchange.svg](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange#/media/File:Diffie-Hellman_Key_Exchange.svg)_

Basically, there are two parties, Alice and Bob, which agree on a starting color (arbitrary but has to be different every time). They also have a secret color they keep to themselves. They then mix this color with the shared color, resulting in two different colors. They then pass this color to the other party, who mixes it with their secret color, resulting in the same ending secret color. 

This relies upon the idea that it's relatively easy to mix two colors together, but it is very difficult to separate them in order to find the secret color. In practice, this is done with mathematics.

For example:

1. Bob and Alice agree on two numbers, a large prime, p = 29, and base g = 5
2. Now Bob picks a secret number, x (x = 4) and does the following: X = g^x % p (in this case % indicates the remainder. For example 3%2 is 3/2, where the remainder is 1). X = 5 ^4 % 29 = 625 % 29 = 16
3. Alice also picks a secret number, y (y = 8) and does the following: Y = g^y % p.  Y = 5 ^ 8 % 29 = 390,625 % 29 = 24
4. Bob sends X to Alice and Alice sends Y to Bob.
5. Then Bob does the following: K = Y^x % p, K = 24 ^ 4 % 29 = 331,776 % 29 = 16
6. Alice then does the following: K = X^y % p, K = 16 ^ 8 % 29 = 4,294,967,296 % 29 = 16

The great (*possibly magic*) thing about this, is that both Bob and Alice have the same number, K, and can now use this to talk secretly, because no one else knows K.

The security of this protocol is predicated on a few things:

1. (Fact) It's relatively easy to generate prime numbers, even large prime numbers (like p).
2. (Fact) Modular exponentiation is easy. In other words, it's relatively easy to compute X = g ^ x % p.
3. (Assumption based on current computing power and mathematics) Modular root extraction without the prime factors is very hard. Essentially, it's very hard to find K without knowing x and y, even if you've snooped on the traffic and can see p, g, X, and Y.

Thus, assuming this was implemented correctly, it's relatively easy to do the math required to create the key, but is extremely difficult and time consuming to do the math required to try to break the key by brute forcing it. 

Even if an attacker could compromise this key, Diffie-Hellman allows for perfect forward secrecy.

### What is perfect forward secrecy?

This is the idea that if you crack the encryption that the server is using to communicate now, it doesn’t mean that all communications that the server has ever carried out are able to be read. 

In other words, it only allows you to see the communications that are being used now (ie with this secret key). Since each set of communications has a different secret key, you would have to crack them all separately. 

This is possible if each session has a different, ephemeral key for each session. Because Diffie-Hellman always uses new random values for each session, (therefore generating new keys for each session) it is called Ephemeral Diffie Hellman (EDH or DHE). Many cipher suites use this to achieve perfect forward secrecy.

As Diffie-Hellman allows you to exchange key material in plaintext without worrying about compromising the shared secret, and the math is too complicated for an attacker to brute force, the attacker can't derive the session key (and even if they could, using different, ephemeral, keys for each session means that they could only snoop on this session - not any in the past or future). 

Forward secrecy is enabled with any Diffie-Hellman key exchange, but only ephemeral key exchange (a different key for every session) provides perfect forward secrecy. 

[Here's a post](https://scotthelme.co.uk/perfect-forward-secrecy/) from Scott Helme talking about this in more depth and explaining how to enable this on your servers.

### What are Diffie-Hellman's limitations?

The biggest limitation of D-H is that is doesn't verify identity. In other words, anyone can claim to be Alice or Bob and there is no built-in mechanism for verifying that their statement is true. 

In addition, if the implementation is not carried out in a secure manner, the algorithm could be cracked with enough dedicated resources (unlikely, but possible for academic teams or nation-state actors). 

For example, this could occur if the random number generator is not provided with adequate entropy to support the desired strength - in other words, because computer generated numbers are never truly random, the degree to which you've artificially injected uncertainness matters to the strength of your implementation.

Additionally, there was an attack demonstrated in 2015 which showed that when the same prime numbers were used by many servers as the beginning of the key exchange, the overall security of Diffie-Hellman was lower than expected. 

Essentially an attacker could simply precompute the attack against that prime, making it easier to compromise sessions for any server which has used that prime number. 

This occurred because millions of servers were using the same prime numbers for key exchanges. Precomputing this type of attack still requires either academic or nation-state level resources and is unlikely to impact the vast majority of people. 

However, luckily for those who have to worry about nation-state attackers, there is a different way to achieve the DH key exchange using elliptic curve cryptography (ECDHE). This is out of the scope of this article, but if you're interested in learning more about the math behind this exchange, check out [this article](https://vincent.bernat.ch/en/blog/2011-ssl-perfect-forward-secrecy).

For a more detailed look at the weaknesses of DH, check out [this whitepaper](https://cert.europa.eu/static/WhitePapers/CERT-EU-SWP_16-002_Weaknesses%20in%20Diffie-Hellman%20Key%20v1_0.pdf) and [this website.](https://weakdh.org/)

## RSA

RSA is named for the creators  –  Rivest, Shamir, Adleman – and it is a manner of generating public and private keys. 

Technically there are two RSA algorithms (one used for digital signatures, and one used for asymmetric encryption.) - this article covers the asymmetric encryption algorithm. 

This allows for key exchange - you first assign each party to the transaction public/private keys, then you generate a symmetric key, and finally, you use the public/private key pairs to securely communicate the shared symmetric key. 

Because asymmetric encryption is generally slower than symmetric encryption, and doesn't scale as well, using asymmetric encryption to securely exchange symmetric keys is very common.

So, how does it work?

1. Pick 2 very large prime numbers (at least 512 bits, or 155 decimal digits each), x and y (these numbers need to be secret and randomly chosen)
2. Find the product, ie z = x*y
3. Select an odd public integer, e, between 3 and n - 1, and has no common factors (other than 1) with (x-1)(y-1) (so it is relatively prime to x - 1 and y - 1).
4. Find the least common multiple of x - 1 and y - 1, and call it L.
5. Calculate the private exponent, d, from x, y, and e. de = 1 % L. d is the inverse of e % L (you know that an inverse exists because e is relatively prime to z - 1 and y - 1). This system works because p = (p ^ e) ^d % z.
6. Output (z, e) as the public key and (z, d) as the private key.

Now, if Bob would like to send a message to Alice, he generates the ciphertext(C) from the plain text(P) using this formula:

C = P^e % z

In order to decrypt this message, Alice computes the following:

P = C^d % z

The relationship between d and e ensures that encryption and decryption functions are inverses. That means that the decryption function is able to successfully recover the original message, and that it's quite hard to recover the original message without the private key (z, d) (or prime factors x and y). 

This also means that you can make z and e public without compromising the security of the system, making it easy to communicate with others with whom you don't already have a shared secret key.

You can also use the operations in reverse to get a digital signature of the message. First, you use the decryption operation on the plaintext. For example, s = SIGNATURE(p) = p ^ d % z.

Then, the recipient can verify the digital signature by applying the encryption function and comparing the result with the message. For example, m = VERIFY(s) = S ^ e % z.

Often when this is done, the plaintext is a hash of the message, meaning you can sign the message (regardless of length) with only one exponentiation.

The security of system is based on a few things: 

1. (Fact) It's relatively easy to generate prime numbers, even large prime numbers (like x and y).
2. (Fact) Multiplication is easy. It's very easy to find z.
3. (Assumption based on current mathematics) Factoring is hard. Given z, it's relatively hard to recover x and y. It is do-able, but it takes a while, and it is expensive.   
  
[One estimate](http://mathaware.org/mam/06/Kaliski.pdf) says that recovering the prime factors of a 1024-bit number would take a year on a machine which cost $10 million. Doubling the size would exponentially increase the amount of work needed (several billion times more work).   
  
As technology continues to advance, these costs (and the work required) will decrease, but at this point, this type of encryption, properly implemented, is an unlikely source of compromise.   
  
Generally the only hackers with this type of money and dedication to a single target are nation-states. Plus, if there's an easier way to compromise a system (see below), that's probably a better option.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/Screen-Shot-2019-10-05-at-11.18.45-AM.png)
_[https://xkcd.com/538/](https://xkcd.com/538/)_

4. (Fact) Modular exponentiation is easy. In other words, it's relatively easy to compute c = p ^ e % z.

5. (Fact) Modular root extraction - reversing the process above - is easy if you have the prime factors (if you have z, c, e, and the prime factors x and y, it's easy to find p such that c = p ^ e % z).

6. (Assumption based on current computing power and mathematics) Modular root extraction without the prime factors is very hard (if you have z, c, e, but not x and y, it's relatively hard to find p such that c = p ^ e % z, particularly if a is sufficiently large).

Want to learn more about the math from much smarter people? Check out [this article.](http://mathaware.org/mam/06/Kaliski.pdf)

## Great, which is better?

It depends on your use case. There are a few differences between the two algorithms - first, perfect forward secrecy (PFS), which we talked about earlier in context of Diffie-Hellman. While technically you _could_ generate ephemeral RSA key pairs, and provide perfect forward secrecy with RSA, the computational cost is much higher than for Diffie-Hellman - meaning that Diffie-Hellman is a better choice for SSL/TLS implementations where you want perfect forward secrecy.  

While there are some performance differences between the two algorithms (in terms of work required from the server), the performance differences generally aren't large enough to make a difference when choosing one over the other. 

Instead, in general, the primary consideration when determining which is better depends on which one is more supported for your use case (for example, when implementing SSL you'll want Diffie Hellman due to perfect forward secrecy) or which is more popular or accepted as the standard in the industry. 

For example, while Diffie-Hellman was US government approved, and supported by an institutional body, the standard wasn't released - whereas RSA (standardized by a private organization) provided a free standard, meaning that RSA became very popular among private organizations. 

If you're interested in reading more, there's a great thread [here](https://security.stackexchange.com/questions/35471/is-there-any-particular-reason-to-use-diffie-hellman-over-rsa-for-key-exchange/35472#35472) on the differences.

Interested in learning how to hackers use cryptographic attacks? Try [this](https://cryptopals.com/) set of challenges from Cryptopals.

%[https://twitter.com/preinheimer/status/841273046317060105?lang=en]


