---
title: 'Diffie-Hellman: The Genius Algorithm Behind Secure Network Communication'
subtitle: ''
author: David Karolyi
co_authors: []
series: null
date: '2020-05-11T18:53:11.000Z'
originalURL: https://freecodecamp.org/news/diffie-hellman-key-exchange
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b21740569d1a4ca29e4.jpg
tags:
- name: algorithms
  slug: algorithms
- name: computer network
  slug: computer-network
- name: Cryptography
  slug: cryptography
- name: cybersecurity
  slug: cybersecurity
- name: JavaScript
  slug: javascript
seo_title: null
seo_desc: 'Let''s start with a quick thought experiment.

  You have a network of 3 computers, used by Alice, Bob, and Charlie. All 3 participants
  can send messages, but just in a way that all other clients who connected to the
  network can read it. This is the only...'
---

Let's start with a quick thought experiment.

You have a network of 3 computers, used by Alice, Bob, and Charlie. All 3 participants can send messages, but just in a way that all other clients who connected to the network can read it. This is the only possible communication form between participants.

If Alice sends a message through the wires, both Bob and Charlie get it. In other words, Alice cannot send a direct message to Bob without Charlie receiving it as well.

But Alice wants to send a confidential message to Bob and doesn't want Charlie to be able to read it.

Seems impossible with these strict rules, right? The beautiful thing that this problem is solved in 1976 by Whitfield Diffie and Martin Hellman.

This is a simplified version of the real world, but we face the same problem when communicating through the biggest network that's ever existed.

Usually, you are not directly connected to the internet, but you are part of a local smaller network, called Ethernet. 

This smaller network can be wired or wireless (Wi-Fi), but the base concept remains. If you send a signal through the network this signal can be read by all other clients connected to the same network.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/network-ethernet.png)

Once you emit a message to your bank's server with your credit card information, all other clients in the local network will get the message, including the router. It will then forward it to the actual server of the bank. All other clients will ignore the message.

But what if there is a malicious client in the network who won't ignore your confidential messages, but read them instead? How is it possible you still have money on your bank account?

## Encryption

It's kind of clear at this point that we need to use some kind of encryption to make sure that the message is readable for Alice and Bob, but complete gibberish for Charlie.

Encrypting information is done by an encryption algorithm, which takes a key (for example a string) and gives back an encrypted value, called ciphertext. The ciphertext is just a completely random-looking string.

It's important that the encrypted value (ciphertext) can be decrypted only with the original key. This is called a symmetric-key algorithm because you need the same key for decrypting the message as it was encrypted with. There are also asymmetric-key algorithms, but we don't need them right now.

To make it easier to understand this, here is a dummy encryption algorithm implemented in JavaScript:

```javascript
function encrypt(message, key) {
    return message.split("").map(character => {
        const characterAsciiCode = character.charCodeAt(0)
    	return String.fromCharCode(characterAsciiCode+key.length)
    }).join("");
}
```

In this function, I mapped each character into another character based on the length of the given key.

Every character has an integer representation, called ASCII code. There is a dictionary that contains all characters with its code, called the ASCII table. So we incremented this integer by the length of the key:

![Image](https://www.freecodecamp.org/news/content/images/2020/05/image-13.png)
_Character mapping_

Decrypting the ciphertext is pretty similar. But instead of addition, we subtract the key length from every character in the ciphertext, so we get back the original message.

```javascript
function decrypt(cipher, key) {
    return cipher.split("").map(character => {
        const characterAsciiCode = character.charCodeAt(0)
    	return String.fromCharCode(characterAsciiCode-key.length)
    }).join("");
}
```

Finally here is the dummy encryption in action:

```javascript
const message = "Hi Bob, here is a confidential message!";
const key = "password";

const cipher = encrypt(message, key);
console.log("Encrypted message:", cipher);
// Encrypted message: Pq(Jwj4(pmzm(q{(i(kwvnqlmv|qit(um{{iom)

const decryptedMessage = decrypt(cipher, key);
console.log("Decrypted message:", decryptedMessage);
// Decrypted message: Hi Bob, here is a confidential message!
```

We applied some degree of encryption to the message, but this algorithm was only useful for demonstration purposes, to get a sense of how symmetric-key encryption algorithms behave. 

There are a couple of problems with this implementation besides handling corner cases and parameter types poorly.

First of all every 8 character-long key can decrypt the message which was encrypted with the key "password". We want an encryption algorithm to only be able to decrypt a message if we give it the same key that the message was encrypted with. A door lock that can be opened by every other key isn't that useful.

Secondly, the logic is too simple – every character is shifted the same amount in the ASCII table, which is too predictable. We need something more complex to make it harder to find out the message without the key.

Thirdly, there isn't a minimal key length. Modern algorithms work with at least 128 bit long keys (~16 characters). This significantly increases the number of possible keys, and with this the secureness of encryption.

Lastly, it takes too little time to encrypt or decrypt the message. This is a problem because it doesn't take too much time to try out all possible keys and crack the encrypted message. 

This is hand in hand with the key length: An algorithm is secure if I as an attacker want to find the key, then I need to try a large number of key combinations and it takes a relatively long time to try a single combination.

There is a wide range of symmetric encryption algorithms that addressed all of these claims, often used together to find a good ratio of speed and secureness for every situation.

The more popular symmetric-key algorithms are [Twofish](http://en.wikipedia.org/wiki/Twofish), [Serpent](http://en.wikipedia.org/wiki/Serpent_%28cipher%29), [AES](http://en.wikipedia.org/wiki/Advanced_Encryption_Standard) ([Rijndael](http://en.wikipedia.org/wiki/Rijndael)), [Blowfish](http://en.wikipedia.org/wiki/Blowfish_%28cipher%29), [CAST5](http://en.wikipedia.org/wiki/CAST5), [RC4](http://en.wikipedia.org/wiki/RC4), [TDES](http://en.wikipedia.org/wiki/Triple_DES), and [IDEA](http://en.wikipedia.org/wiki/International_Data_Encryption_Algorithm).

If you want to learn more about cryptography in general check out [this talk](https://www.youtube.com/watch?v=cqgtdkURzTE).

## Key exchange

It looks like we reduced the original problem space. With encryption, we can create a message which is meaningful for parties who are eligible to read the information, but which is unreadable for others.

When Alice wants to write a confidential message, she would pick a key and encrypt her message with it and send the ciphertext through the wires. Both Bob and Charlie would receive the encrypted message, but none of them could interpret it without Alice's key.

Now the only question to answer is how Alice and Bob can find a common key just by communicating through the network and prevent Charlie from finding out that same key.

If Alice sends her key directly through the wires Charlie would intercept it and would be able to decrypt all Alice's messages. So this is not a solution. This is called the key exchange problem in computer science.

### Diffie–Hellman key exchange

This cool algorithm provides a way of generating a shared key between two people in such a way that the key can't be seen by observing the communication.

As a first step, we'll say that there is a huge prime number, known to all participants, it's public information. We call it **"p" or modulus**. 

There is also another public number called **"g" or base**, which is less than **p**. 

Don't worry about how these numbers are generated. For the sake of simplicity let's just say Alice picks a very big prime number (**p**) and a number which is considerably less than **p**. She then sends them through the wires without any encryption, so all participants will know these numbers.

**Example:** To understand this through an example, we'll use small numbers. Let's say **p=23** and **g=5**.

As a second step both Alice (**a**) and Bob (**b**) will pick a secret number, which they won't tell anybody, it's just locally living in their computers.

**Example:** Let's say Alice picked 4 (**a=4**), and Bob picked 3 (**b=3**).

As a next step, they will do some math on their secret numbers, they will calculate:

1. the base (**g**) in the power of their secret number,
2. and take the calculated number's modulo to **p**.
3. Call the result **A** (for Alice) and **B** (for Bob).

Modulo is a simple mathematical statement, and we use it to find the remainder after dividing one number by another. Here is an example: **23 mod 4 = 3**, because 23/4 is 5 and 3 remains.

Maybe it's easier to see all of this in code:

```javascript
// base
const g = 5;
// modulus
const p = 23;

// Alice's randomly picked number
const a = 4;
// Alice's calculated value
const A = Math.pow(g, a)%p;

// Do the same for Bob
const b = 3;
const B = Math.pow(g, b)%p;

console.log("Alice's calculated value (A):", A);
// Alice's calculated value (A): 4
console.log("Bob's calculated value (B):", B);
// Bob's calculated value (B): 10
```

Now both Alice and Bob will send their calculated values (**A**, **B**) through the network, so all participants will know them.

As a last step Alice and Bob will take each other's calculated values and do the following:

1. Alice will take Bob's calculated value (**B**) in the power of his secret number (**a**),
2. and calculate this number's modulo to **p** and will call the result **s** (secret).
3. Bob will do the same but with Alice's calculated value (**A**), and his secret number (**b**).

At this point, they successfully generated a common secret (**s**), even if it's hard to see right now. We will explore this in more detail in a second.

In code:

```javascript
// Alice calculate the common secret
const secretOfAlice = Math.pow(B, a)%p;
console.log("Alice's calculated secret:", secretOfAlice);
// Alice's calculated secret: 18

// Bob will calculate
const secretOfBob = Math.pow(A, b)%p;
console.log("Bob's calculated secret:", secretOfBob);
// Bob's calculated secret: 18
```

As you can see both Alice and Bob got the number 18, which they can use as a key to encrypt messages. It seems magic at this point, but it's just some math. 

Let's see why they got the same number by splitting up the calculations into elementary pieces:

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-09-at-12.11.18.png)
_The process as an equation_

In the last step, we used a [modulo arithmetic identity](https://en.wikipedia.org/wiki/Modulo_operation#Properties_(identities)) and its distributive properties to simplify nested modulo statements.

So Alice and Bob have the same key, but let's see what Charlie saw from all of this. We know that **p** and **g** are public numbers, available for everyone. 

We also know that Alice and Bob sent their calculated values (**A**, **B**) through the network, so that can be also caught by Charlie.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-09-at-20.12.35.png)
_Charlie's perspective_

Charlie knows almost all parameters of this equation, just **a** and **b** remain hidden. To stay with the example, if he knows that **A** is 4 and **p** is 23, **g** to the power of **a** can be 4, 27, 50, 73, ... and infinite other numbers which result in 4 in the modulo space.

He also knows that only the subset of these numbers are possible options because not all numbers are an exponent of 5 (**g**), but this is still an infinite number of options to try.

This doesn't seem too secure with small numbers. But at the beginning I said that **p** is a really large number, often 2000 or 4000 bits long. This makes it almost impossible to guess the value of **a** or **b** in the real world.

The common key Alice and Bob both possess only can be generated by knowing **a** or **b**, besides the information that traveled through the network.

If you're more visual, here is a great diagram shows this whole process by mixing buckets of paint instead of numbers.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Diffie-Hellman_Key_Exchange.svg)
_source: [Wikipedia](https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange)_

Here **p** and **g** shared constants represented by the yellow "Common paint". Secret numbers of Alice and Bob (**a**, **b**) is "Secret colours", and "Common secret" is what we called **s**.

This is a great analogy because it's representing the irreversibility of the modulo operation. As mixed paints can't be unmixed to their original components, the result of a modulo operation can't be reversed.

## Summary

Now the original problem can be solved by encrypting messages using a shared key, which was exchanged with the Diffie-Hellman algorithm. 

With this Alice and Bob can communicate securely, and Charlie cannot read their messages even if he is part of the same network.

Thanks for reading this far! I hope you got some value from this post and understood some parts of this interesting communication flow.

If it was hard to follow the math of this explanation, [here](https://www.youtube.com/watch?v=NmM9HA2MQGI) is a great video to help you understand the algorithm without math, from a higher level.

If you liked this post, you may want to follow me on [Twitter](https://twitter.com/karolyidav) to find some more exciting resources about programming and software development.

