---
title: How Homomorphic Encryption Works – Explained in Plain English
subtitle: ''
author: Tiago Capelo Monteiro
co_authors: []
series: null
date: '2024-01-29T18:33:48.000Z'
originalURL: https://freecodecamp.org/news/homomorphic-encryption-in-plain-english
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/vanna-phon-hRXIKdxoaPo-unsplash--1-.jpg
tags:
- name: encryption
  slug: encryption
- name: information security
  slug: information-security
seo_title: null
seo_desc: "As the fields of cryptography and cybersecurity advance, homomorphic encryption\
  \ stands out as a groundbreaking technology. \nIt has the potential to reshape everything\
  \ in data privacy and security.\nWhat really is homomorphic encryption? Why is it\
  \ gett..."
---

As the fields of cryptography and cybersecurity advance, [homomorphic encryption](https://www.freecodecamp.org/news/introduction-to-homomorphic-encryption/) stands out as a groundbreaking technology. 

It has the potential to reshape everything in data privacy and security.

What really is homomorphic encryption? Why is it getting so much attention? How can it increase data privacy?

Essentially, with homomorphic encryption, we can process encrypted data without ever needing to decrypt it for computation.

This results in complete privacy everywhere the data is processed and stored.

In this article, you'll learn why this type of encryption will revolutionize the field of security. We'll tackle questions such as:

* What is homomorphic encryption?
* How does homomorphic encryption work?
* Homomorphic encryption vs traditional encryption – what's the difference?
* What are the applications of homomorphic encryption?

## What is Homomorphic Encryption?

Let's use an analogy to understand homomorphic encryption.

Imagine a locked treasure chest that has many valuable items inside.

To add or remove items, you need to unlock the chest. This could make it easier for thieves to steal the items when you open it.

In this analogy, this is what traditional encryption is.

Homomorphic encryption is like having a magical glove that allows you to add or remove items from the chest without ever unlocking it.

This way, you remove the risk of thieves ever getting the items inside the treasure chest.

This is essentially what Homomorphic encryption does with data: it allows us to perform operations on encrypted data without ever needing to decrypt it.

This is not possible with traditional encryption. In that case, we must process the data we need to decrypt, do whatever computations are necessary, and then encrypt the data again.

With homomorphic encryption, security is never compromised.

## How Does Homomorphic Encryption Work?

Homomorphic encryption allows computations to act on encrypted data – also called ciphertext.

This means the data is processed while encrypted.

Homomorphic encryption does computations on encrypted data (ciphertext). But computations done in ciphertext give encrypted results.

When these results are decrypted, they are similar to those that would've been obtained if the operations had been performed on the original, unencrypted data.

So basically, homomorphic encryption allows operations on encrypted data to give the same results as if performed on the original, decrypted data.

### How is this done?

Homomorphic encryption uses complex mathematical algorithms that:

* transform the numbers to obscure the original data, and 
* perform the same operations whether on the original or on this obscured data.

Essentially, you're always working on the same data in the same way, but from different points of view.

So you can work with the data and get exactly the same results as if it were not encrypted. But since it actually is encrypted, the data is always protected!

This way, no one can see it and maybe steal it, which allows data privacy even in environments where trust is minimal.

### Python code example

We are going to use the Pyfhel library for this example, which you can read more about [here](https://pypi.org/project/Pyfhel/3.1.1/).

In this code, we are going to add two numbers in their encrypted form and see the results.

Here is the full code so you can truly understand how homomorphic encryption works:

```python
import numpy as np
from Pyfhel import Pyfhel

HE = Pyfhel()
HE.contextGen(scheme='bfv', n=2**14, t_bits=20)
HE.keyGen()

integer1 = np.array([127], dtype=np.int64)
integer2 = np.array([-57], dtype=np.int64)

ctxt1 = HE.encryptInt(integer1)
ctxt2 = HE.encryptInt(integer2)

ctxtSum = ctxt1 + ctxt2
ctxtSub = ctxt1 - ctxt2
ctxtMul = ctxt1 * ctxt2

resSum = HE.decryptInt(ctxtSum) 
resSub = HE.decryptInt(ctxtSub)
resMul = HE.decryptInt(ctxtMul)
```

![Image](https://www.freecodecamp.org/news/content/images/2024/01/ray-so-export.png)

Now we are going to break it down line by line:

First, we need to import the necessary modules:

```
import numpy as np
from Pyfhel import Pyfhel
```

Here, we are just importing the necessary modules to make our calculations.

Next, we need to create a Pyfhel object and generate keys:

```
HE = Pyfhel()
HE.contextGen(scheme='bfv', n=2**14, t_bits=20)
HE.keyGen()
```

In the first line we initialize a `Pyfhel` python object. In the second line we set encryption with certain parameters:

* `scheme='bfv'`: We use the [BFV (Brakerski/Fan-Vercauteren)](https://link.springer.com/chapter/10.1007/978-3-030-92078-4_21) homomorphic encryption scheme.
* `n=2**14`: Defines the degree of the polynomial modulus degree. The polynomial modulus degree balances the encryption security level with the computational efficiency. A bigger number gives better encryption but at the cost of more computational resources
* `t_bits=20`: Sets the bit size of the plaintext modulus. Bigger bit size values let you use larger numbers but make the encryption less clean
* In the third line, we [generate a public and private key](https://www.freecodecamp.org/news/encryption-explained-in-plain-english/)

Then, we get two numbers and encrypt them:

```
integer1 = np.array([127], dtype=np.int64)
integer2 = np.array([-57], dtype=np.int64)

ctxt1 = HE.encryptInt(integer1)
ctxt2 = HE.encryptInt(integer2)
```

We represent the numbers in a array with just one number and encrypt them.

We represent these numbers in an array and not as if we are declaring variables.

We do this because the function `encryptInt()` only takes an array of integers with 64 bits as an argument. From the [documentation](https://pyfhel.readthedocs.io/en/latest/_autosummary/Pyfhel.Pyfhel.html):

```python
encryptInt(self, int64_t[:] arr, PyCtxt ctxt=None)
```

Now we'll perform the operations on the two numbers while encrypted:

```
ctxtSum = ctxt1 + ctxt2
ctxtSub = ctxt1 - ctxt2
ctxtMul = ctxt1 * ctxt2
```

And then decrypt the numbers after the operation when they where encrypted:

```
resSum = HE.decryptInt(ctxtSum) 
resSub = HE.decryptInt(ctxtSub)
resMul = HE.decryptInt(ctxtMul)
```

Which will output the following:

```
>>> [70  0  0 ...  0  0  0]
>>> [184   0   0 ...   0   0   0]
>>> [-7239     0     0 ...     0     0     0]
```

And if we do the normal calculations without being encrypted, we see that the values match:

```
integer1 = 127
integer2 = -57

print(integer1+integer2)

print(integer1-integer2)

print(integer1*integer2)
```

Which gives the following:

```
>>> 70

>>> 184

>>> -7239
```

As you can see, we get the same results if we perform the operations on the data while it's encrypted as we do when it's not encrypted.

## Homomorphic Encryption vs Traditional Encryption – What's the Difference?

In traditional encryption methods, data needs to be decrypted before any kind of processing. 

In homomorphic encryption, data is always used in its encrypted state.

Traditional encryption is like a secure envelope: contents must be taken out to be read or modified. 

Homomorphic encryption is like a special envelope that allows content manipulation without ever needing to open it to be read or modified.

## Applications of Homomorphic Encryption

There are many practical applications of homomorphic encryption.

In cloud computing, it allows users to process data in the cloud without ever exposing it to cloud service providers. This way, sensitive information always remains confidential.

In healthcare, it allows the analysis of encrypted medical records without compromising patient privacy. Patient health data always remains protected.

Another promising application of homomorphic encryption is in secure voting systems. Using this type of encryption, votes are counted in such a way that no one can see for whom each person voted. This would make the voting process safer and more private.

These examples represent just the tip of the iceberg. 

## Conclusion

Homomorphic encryption is a paradigm shift in how we handle and process sensitive data. 

This technology and its development are important as more and more data breaches are happening all the time.

Homomorphic encryption offers a path toward the simplification of data privacy regulations. 

It also allows more innovation by making the protection of private data simpler, encouraging new security developments.


