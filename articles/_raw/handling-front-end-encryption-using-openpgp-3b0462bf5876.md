---
title: Handling front-end encryption using OpenPGP
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-17T04:10:48.000Z'
originalURL: https://freecodecamp.org/news/handling-front-end-encryption-using-openpgp-3b0462bf5876
coverImage: https://cdn-media-1.freecodecamp.org/images/1*HMRjFON6A7nGDlvrf7auIw.png
tags:
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Mateja Trifunovski

  In a world where privacy is being constantly invaded, people tend to start to care
  about it. Private messaging platforms are becoming more and more popular. They should
  be, because privacy does matter.

  This article will be about...'
---

By Mateja Trifunovski

In a world where privacy is being constantly invaded, people tend to start to care about it. Private messaging platforms are becoming more and more popular. They should be, because privacy does matter.

This article will be about email end-to-end encryption. My experience comes from building a decentralized end-to-end encrypted email system called [**Lemon Email**](https://lemon.email/). The email encryption can apply to pretty much any system, using the same or similar cryptographic algorithms.

### So what is front-end encryption?

The basic idea is that to retain the privacy of the data, we need to make it unreadable to possible intruders. The best way to do that is to encrypt it at the source, that is, at the client side. We need to make sure that even if the data gets intercepted on it’s way to the server or a database, it is impossible to distinguish what that piece of data is.

### **So how do we do it?**

We will be using a cryptographic system called [Public-key cryptography](https://en.wikipedia.org/wiki/Public-key_cryptography) , also known as asymmetric cryptography. For actual implementation we will be using an open source library [OpenPGP.js](https://github.com/openpgpjs/openpgpjs). The implementation will be very simple, omitting any back-end code due to simplicity.

#### Generating keys

The first step is to generate our private and public keys which we will use to encrypt/decrypt our emails. In the code snippet below we add some options like how long is the key. The length of the key will determine the key’s strength and also the time to generate it. We also add a user-specified **passphrase** used to lock the private key.

```js
let keyOptions = {
    numBits: 2048,
    passphrase: "secret-passphrase"
    //you would get the passphrase from an input field normally
};

let user = {};

openpgp.generateKey(keyOptions)
    .then((key) => {
        user.privateKey = key.privateKeyArmored;
        user.publicKey = key.publicKeyArmored;
    });
```

The **passphrase** is very important since the private key can’t be used without it. It’s the only thing preventing other people from using the private key. This is useful because we usually store our private key in persistent storage, such as a database, where someone can see it. The passphrase should be only remembered on the client side, in the user’s memory.

#### Encrypting a message

After creating our keys, in order for users to exchange messages, well we need at least two users. So for simplicity sake let’s say another user created his keys somewhere and we now have two users.

In this scenario a user named Bob is sending a message to John. If we want only John to be able to read the message, we get John’s **public key** and use it to encrypt the full message. Later John will be able to read the message using his **private key.**

```js
// Bob{} (User 1), John{} (User 2)
const email = {
    subject: "Hello John, I'm Bob!",
    body: "Secret message"
}

const options = {
    data: JSON.stringify(email),
    // Here we use John's public key for encryption
    publicKeys:  openpgp.key.readArmored(John.publicKey).keys
};

let messageForJohn = "";
openpgp.encrypt(options)
    .then((cipherText)=>{
         messageForJohn = cipherText.data;
    });
```

The variable `messageForJohn` which holds the encrypted value of the email which now looks like the snippet below.

```js
-----BEGIN PGP MESSAGE-----
Version: OpenPGP.js v2.5.4
Comment: http://openpgpjs.org

0mgBCFDGPx2Bz+cETU+PtCjKSzgB+U4pVvEakBlEdBHFnccqfSBI8+A1DCns
s1cOKrMtJ5SfZaYSlxdO+982UqgH8NEV5/+ZLn8OCx+/ppff4EIuN0ZuN4ps
LkbeHL93oA8Ja/rKGJp+kg==
=bf0/
-----END PGP MESSAGE-----
```

#### **Decrypting a message**

Now that we have the contents of the message encrypted, we should decrypt it so John can finally see his message. Now all we need is John’s **passphrase** (“john-passphrase”) and his **private key**.

```js
// John {} (User 2) 
let privateKey = openpgp.key.readArmored(John.privateKey).keys[0];

if (privateKey.decrypt("john-passphrase")) {
    openpgp.decrypt({
        privateKey: privateKey,
        message: openpgp.message.readArmored(messageForJohn)
    })
    .then((decryptedData) => {
        decryptedData = JSON.parse(decryptedData.data);
        console.log(decryptedData);
    })
}
```

John’s message has been decrypted and he can read it now. If everything went well it should look like this.

```json
{
  "subject": "Hello John, I'm Bob!",
  "body": "Secret message"
}
```

#### Further steps

This was a brief demonstration of how two users can communicate privately. You can expand it according to your wishes. Try storing the public and private keys in a database, and create a login system that requires a user to enter a passphrase along the usual username and password. You could also try using other encryption libraries like [crypto-js](https://github.com/brix/crypto-js), just play with it!

### Caveats

At first, might you think, “why isn’t everything encrypted?” Well, there are some drawbacks that come with encryption.

Clients like browsers are becoming more and more performant. Having only one main thread, the screen can freeze when doing intensive work like generating keys, or decrypting large data. Of course with web workers and future performance updates, this could become a standard.

Also, some features like search can become quite tricky, because you can’t easily search through encrypted data. But with new technologies like [IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API) we might even see fully front-end search soon.

### **Conclusion**

I’ve made an example showing basic encryption of a dummy email at this [Github Link](https://github.com/Matko95/front-end-encryption-example). So feel free to take a look at the code and play around with it!

