---
title: What is Homomorphic Encryption?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-26T23:01:28.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-homomorphic-encryption
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/Homomorphic-Encryption-3--1.png
tags:
- name: cybersecurity
  slug: cybersecurity
- name: encryption
  slug: encryption
seo_title: null
seo_desc: "By Aris Zagakos\nIn this article we will discuss Homomorphic Encryption,\
  \ the problem that it solves, and the different types that exist. \nThen we will\
  \ write code in Python to show some of its capabilities in action.\nHere's what\
  \ we'll cover:\n\nWhat is H..."
---

By Aris Zagakos

In this article we will discuss Homomorphic Encryption, the problem that it solves, and the different types that exist. 

Then we will write code in Python to show some of its capabilities in action.

## Here's what we'll cover:

1. What is Homomorphic Encryption?
2. Advantages of Homomorphic Encryption
3. Types of Homomorphic Encryption
4. Paillier Cryptosystem
5. Conclusion and resources to learn more

## What is Homomorphic Encryption?

The name Homomorphic comes from the algebra term Homomorphism.

> "Homomorphism is a structure-preserving map between two algebraic structures of the same type (such as two groups, two rings, or two vector spaces)." (Source: Wikipedia<ins>)</ins>

`Homomorphic Encryption` is a form of encryption that allows users to perform binary operations on encrypted data without ever decrypting the data. 

This form of encryption allows information to be encrypted and outsourced to cloud services/environments for processing, without accessing the raw data.

## Advantages of Homomorphic Encryption

In today's world, if we want to perform computations on encrypted data such as mathematical operations, we have to decrypt them first. Then we have to make our computations, and finally encrypt the data again in order to send them back.

But what happens when the encrypted data is very sensitive and we don't want other services to have access to them? Here is where `Homomorphic encryption` comes into play.

A more practical example would be a system/service that processes medical information in order to diagnose if a patient has a condition or not.

The data we'd be sharing probably includes very sensitive information about the patient's medical history. So this is something we want to ensure won't be accessible to anyone else.

Using `Homomorphic Encryption`, the system/service can process the required computations on the encrypted data, returning the result of the diagnosis without knowing which information is being proceeded.

Sharing sensitive information through different platforms gives away our privacy. On the other hand, being able to modify and perform operations on data while they are encrypted ensures the privacy of the data.

## Types of Homomorphic Encryption

The goal of Homomorphic Encryption is the following: given any input such as  
`input := Enc(x1),...,Enc(xn)`, for any arbitrary function `f` that applies an infinite number of additions or multiplications such as `value := f(Enc(x1),...,Enc(xn))`, the value can be computed while the input is encrypted.

The arithmetic operations, at the end of the day, are implemented at the hardware level (as anything else) under arithmetic or boolean circuits. 

The operations that we want to perform are Homomorphic Addition and Homomorphic Multiplication. The names Addition and Multiplication are given due to the similar behavior of binary addition and binary multiplication that logic gates XOR and AND have correspondingly. The combination of these two gates can represent any boolean function.

The factors make the complexity to be varied based on the number and the kind of operations.

Because of these restrictions and the problem of constructing a fully Homomorphic Encryption algorithm (supporting both Homomorphic Addition and Homomorphic Multiplication), over time there have been different schemes implemented.

The most common types of Homomorphic encryption are:

* Partially Homomorphic Encryption (PHE)
* Somewhat Homomorphic Encryption (SHE)
* Fully Homomorphic Encryption (FHE)

Partial Homomorphic Encryption (PHE) allows only one operation to be performed on the ciphertext an infinite number of times. This operation can be only addition or only multiplication. 

Partially Homomorphic Encryption algorithms are easier to design and are very useful in applications that use one arithmetic operation.

Somewhat Homomorphic Encryption (SHE) allows both addition and multiplication to be performed, but for a limited number of times. This limitation is evaluated to a certain depth in the circuit logic. This is a very important milestone to reach Fully Homomorphic Encryption.

Fully Homomorphic Encryption (FHE) allows both addition and multiplication to be performed on the ciphertext an infinite number of times, supporting arbitrary computations on encrypted data. 

The major problem with Fully Homomorphic Encryption is the cost efficiency both in terms of speed and storage requirements compared to plaintext operations.

## Paillier Cryptosystem

The Paillier Cryptosystem was invented by Pascal Paillier in 1999. It is a Partial Homomorphic Encryption (PHE) scheme and Additively Homomorphic. 

It supports only the addition of two ciphertexts and not the multiplication between them. Also, a plaintext number can be added or multiplied to the ciphertext.

In this example we use `python-paillier`, a Python library for Partially Homomorphic Encryption using the Paillier cryptosystem.

```python
from phe import paillier

num1 = 10
num2 = 20

pub_key, priv_key = paillier.generate_paillier_keypair()
cipher_num1, cipher_num2 = pub_key.encrypt(num1), pub_key.encrypt(num2)

# add two encrypted numbers together
result = cipher_num1 + cipher_num2
result = priv_key.decrypt(result)
print("add two encrypted numbers together:",result)

# add an encrypted number to a plaintext number
result = cipher_num1 + 5
result = priv_key.decrypt(result)
print("add an encrypted number to a number:",result)

# multiply an encrypted number by a plaintext number
result = cipher_num1 * 10
result = priv_key.decrypt(result)
print("multiply an encrypted number to a number:",result)

```

In the example above we generated a key pair of a public and a private key. Next, we encrypted both `num1` and `num2` with the public key and performed operations on their ciphertexts.

First, we added the two ciphers. After that, we took the `cipher_num1` and added to it a plaintext number. Last, we did the same process as before, but instead of addition, we multiplied the `cipher_num1` with a plaintext number this time. 

The calculation of these operations takes place while the data is encrypted. Also, we can verify the integrity of the result each time by decrypting it using the private key.

## Conclusion

Homomorphic Encryption (HE) looks like a dream when it comes to data privacy and protection. But its poor performance and high costs still keep it out of commercial/production applications. 

But there have been many improvements in terms of speed lately. With the current pace, I believe that it will be adapted worldwide during the next years.

### Resources

* [Homomorphism](https://en.wikipedia.org/wiki/Homomorphism)
* [Homomorphic encryption](https://en.wikipedia.org/wiki/Homomorphic_encryption)
* [Paillier cryptosystem](https://en.wikipedia.org/wiki/Paillier_cryptosystem)
* [python-paillier](https://python-paillier.readthedocs.io/en/develop/)


