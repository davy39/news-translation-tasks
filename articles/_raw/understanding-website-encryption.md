---
title: How Website Encryption Works
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-03-28T17:35:27.000Z'
originalURL: https://freecodecamp.org/news/understanding-website-encryption
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/pexels-markus-spiske-225769.jpg
tags:
- name: encryption
  slug: encryption
- name: Security
  slug: security
seo_title: null
seo_desc: It's one thing to protect your data when it's sitting quietly on your own
  local machine and not bothering anyone. But moving data between locations – as you
  do whenever you open a website on a remote server or send an email attachment across
  the inte...
---

It's one thing to protect your data when it's sitting quietly on your own local machine and not bothering anyone. But moving data between locations – as you do whenever you open a website on a remote server or send an email attachment across the internet – introduces a whole new set of vulnerabilities.

Plain text protocols transmit data in its unencrypted form, which makes it vulnerable to eavesdropping and tampering by third-party actors. Data transmitted over plain text protocols can be easily intercepted and read by anyone with access to the network. 

If you're thinking of transmitting, say, credit card information or entering online banking passwords this way, then I would beg you to stop right now. You definitely want to add some encryption to your mix.

This article comes from [The Complete LPI Security Essentials Exam Study Guide](https://www.udemy.com/course/complete-lpi-security-essentials-exam-study-guide/?referralCode=C2B6802EDB99578238B5). You can also follow along using this video:

%[https://www.youtube.com/watch?v=v3Z0IRzTEcY&list=PLSiZCpRYoTZ7wEwmKRsRjaQF3qSi4bbdl&index=1]

## Some Key Encryption Protocols

Transport encryption protocols, as it turns out, use encryption techniques to protect the data during transit. The data is encrypted before it is transmitted and decrypted after it is received. This provides protection against eavesdropping and tampering by third-party actors. 

The most common transport encryption protocols are Secure Sockets Layer (SSL) and its successor, Transport Layer Security (TLS).

Beyond transport encryption, end-to-end encryption refers to a method of encrypting data from the sender's device to the recipient's device, such that only the sender and the recipient have access to the data. 

E2EE provides protection for the entire transmission, including protection from intermediaries such as network administrators, service providers, and hackers. E2EE is typically used in applications such as instant messaging, email, and file sharing.

[HTTPS (the Hypertext Transfer Protocol Secure)](https://www.freecodecamp.org/news/what-is-https-http-vs-https-meaning-and-how-it-works/) is a protocol that is commonly used to secure web pages. It uses SSL or TLS encryption to secure the connection between a web browser and a server, ensuring that sensitive information, such as login credentials and credit card numbers, cannot be intercepted by third-party actors.

[TLS (Transport Layer Security)](https://www.freecodecamp.org/news/what-is-tls-transport-layer-security-encryption-explained-in-plain-english/) is a security protocol that provides encryption and integrity for data transmission over the internet. It is the successor to SSL and is currently widely used to secure web connections, email, and other internet protocols. TLS uses public-key cryptography to negotiate a shared secret key, which is then used to encrypt the data.

## How to Identify Website Encryption

You can identify if a website is encrypted by looking for the padlock icon and the "https" prefix in the URL of the website. The padlock icon is usually located in the address bar of your web browser and indicates that the connection between your browser and the website is secure. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-28-at-10.11.06-AM.png)
_The padlock showing that freecodecamp.org/news is secure_

The padlock icon can also show the level of security, such as the type of encryption used, the identity of the website, and the validity of the SSL/TLS certificate.

The "https" prefix in the URL of the website indicates that the connection is encrypted and secure. The "s" in "https" stands for "secure". In contrast, unencrypted websites use the "http" prefix in their URL.

It's important to note that while the padlock icon and the "https" prefix indicate that a website is encrypted, they don't guarantee the authenticity or security of the website. Always be cautious when entering sensitive information, such as login credentials or credit card numbers, into any website and make sure to verify the identity of the website before entering any sensitive information.

TLS-encrypted websites can acquire padlocks and "HTTPS" as a URL prefix by requesting a certificate from a certificate authority. Once upon a time, CAs would charge good money for issuing certificates, and they would take their time about it, too. However, that was before Let's Encrypt.

[Let's Encrypt](https://letsencrypt.org/) is a non-profit certificate authority that provides free, automated, and open-source SSL/TLS certificates. These certificates are used to encrypt and secure web communications, providing privacy and data integrity to internet users. 

The main value of Let's Encrypt is its ability to make encryption more accessible and affordable. By offering free SSL/TLS certificates, Let's Encrypt makes it easier and more cost-effective for website owners to secure their websites and protect the privacy of their users.

In addition to being free, Let's Encrypt certificates are also easy to obtain and install. The certificates are issued through [an automated process](https://certbot.eff.org/), making it possible for website owners to obtain a certificate in minutes, rather than waiting for days or weeks for manual processing.

## Understanding X.509 Certificates

Let's understand those certificates a bit better. X.509 is a standard for digital certificates that is widely used on the internet to establish trust between parties. 

An X.509 certificate is a digital document that contains information about the identity of an entity and is signed by a trusted third-party known as a certificate authority (CA).

![Image](https://www.freecodecamp.org/news/content/images/2023/03/slide-31-1.png)
_Diagram of how X.509 certificates work_

The process of obtaining an X.509 certificate involves jumping through some hoops:

* The entity seeking the certificate (a website owner, for instance) generates a certificate signing request (CSR) which includes information about their identity and public key.
* The CA verifies the identity of the entity and issues the X.509 certificate. The certificate includes the public key of the entity, information about the identity, and the signature of the CA.
* The entity installs the certificate on their web server and configures their website to use HTTPS, which enables encrypted communication between the server and the client.

The process of revoking an X.509 certificate involves the following steps:

* The entity or the CA detects that the certificate needs to be revoked. For example, the entity may have lost control of their private key, or the identity information in the certificate may have changed.
* The entity or the CA requests the revocation of the certificate.
* The CA updates its certificate revocation list to indicate that the certificate has been revoked. The CRL is a list of all the revoked certificates that the CA has issued.
* When a client connects to a website, it checks the certificate against the CRL to make sure it has not been revoked. If the certificate has been revoked, the client will not trust the website and will not establish a secure connection.

An X.509 certificate contains several key fields that provide information about the identity of the entity and the certificate itself. Some of the key fields are:

* The version number of the X.509 certificate format.
* A unique identifier assigned to the certificate by the certificate authority (CA).
* Information about the entity that the certificate represents, such as its name, address, and public key.
* Information about the CA that issued the certificate, such as its name and address.
* The start and end dates of the certificate's validity period, during which the certificate can be trusted.
* The public key of the entity that the certificate represents.
* The algorithm used by the CA to sign the certificate and verify its authenticity.
* The signature of the CA, which is used to verify the authenticity of the certificate.

## Perfect Forward Secrecy (PFS)

There's one more thing we should touch on before leaving the world of encrypted web sessions. Perfect Forward Secrecy (PFS) is a security property in cryptography that ensures that the confidentiality of past sessions cannot be compromised even if the encryption keys used in those sessions are later disclosed. 

This is achieved by using ephemeral keys, which are generated for each session and discarded after the session is completed. The ephemeral keys are used to establish a secure key exchange, and are never stored, so they cannot be used to decrypt past sessions even if they are later disclosed. 

PFS is an important property in secure communication protocols, as it ensures that even if an attacker is able to obtain the encryption keys for a single session, they will not be able to use those keys to compromise past or future sessions.

## Wrapping Up

With this knowledge of encryption's inner workings, you'll be better able to assess the safety of your internet browsing activities. You'll also know what you need to do to encrypt the websites you yourself might manage.

This article and the accompanying video are excerpted from [my Complete LPI Security Essentials Exam Study Guide course](https://www.udemy.com/course/complete-lpi-security-essentials-exam-study-guide/?referralCode=C2B6802EDB99578238B5). And there's much more technology goodness available at [bootstrap-it.com](https://bootstrap-it.com/)

