---
title: What is Encryption at Rest? Explained for Security Beginners
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-04-04T15:49:01.000Z'
originalURL: https://freecodecamp.org/news/encryption-at-rest
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/pexels-cottonbro-studio-7319078.jpg
tags:
- name: encryption
  slug: encryption
- name: information security
  slug: information-security
seo_title: null
seo_desc: 'Encryption is a technique for secure communication that converts plain
  text into a coded form that can only be deciphered with a secret key. Let''s explore
  some of encryption''s fun bits.

  Encryption works by using an algorithm to convert plaintext into...'
---

Encryption is a technique for secure communication that converts plain text into a coded form that can only be deciphered with a secret key. Let's explore some of encryption's fun bits.

Encryption works by using an algorithm to convert plaintext into ciphertext, which is unreadable without a corresponding decryption key. 

This article comes from [The Complete LPI Security Essentials Exam Study Guide](https://www.udemy.com/course/complete-lpi-security-essentials-exam-study-guide/?referralCode=C2B6802EDB99578238B5). You can also follow along with this video:

%[https://www.youtube.com/watch?v=kWBLfhf8eto&list=PLSiZCpRYoTZ7wEwmKRsRjaQF3qSi4bbdl&index=2]

The encryption process takes the original data, and transforms it in a way that only someone with the correct decryption key can reverse the process and read the original data. This helps ensure that sensitive information is protected from unauthorized access or interception during transmission or storage.

## Understanding Encryption Tools

Encryption at rest refers to the practice of protecting data that is stored on a device, such as a hard drive or a smartphone, by encoding it using encryption algorithms. The encrypted data can only be decrypted with the appropriate key, and this helps ensure that sensitive information remains confidential even if the device is lost or stolen. 

This is a common security measure used to protect sensitive information such as credit card numbers, personal data, and confidential business information.

Password hashing is a technique for storing passwords in a secure manner by converting them into a cryptographic representation called a hash. The hash is created using a one-way function that transforms the password into a fixed-length string of characters that cannot be easily reversed to reveal the original password.

```
$ echo -n mySecretPassword | sha256sum
2250e74c6f823de9d70c2222802cd059dc970f56ed8d41d5d22d1a6d4a2ab66f  -

```

Salting is a security measure added to password hashing to increase its resilience against attacks. A salt is a random value that is generated for each password and combined with the password before it is hashed. 

```
$ openssl passwd -salt 29 mytext
$1$29$WKQPJOxDf2nJLoPwT6cnz1
```

This results in a unique hash for each password, even if multiple users have the same password, making it much more difficult for an attacker to use pre-computed tables of hashes (such as rainbow tables) to crack the passwords. 

When verifying a password, the salt is used to regenerate the hash, which is then compared to the stored hash to determine if the password is correct.

## Password Attack Tools

A rainbow table is a pre-computed table of hashes used to crack passwords by searching for a matching hash value. It is an optimization of a brute force attack that reduces the number of hashes that need to be calculated by reusing hashes computed for previous password guesses.

A Directory attack is a method of cracking passwords by using a large dictionary of words, phrases, and commonly used passwords to generate hashes and compare them to the target hashes. This type of attack is effective against weak passwords that are easily guessable.

A brute force attack is a way of cracking passwords by trying all possible combinations of characters until a match is found. It is a slow and resource-intensive method of cracking passwords, but it is effective against strong passwords that cannot be easily guessed. 

Brute force attacks can be mitigated by using strong passwords, rate-limiting login attempts, and using encryption and hashing to store passwords securely.

## Symmetric and Asymmetric Encryption

Symmetric cryptography, also known as shared-secret cryptography, is a type of encryption where the same key is used for both encryption and decryption of data. This means that both the sender and receiver of the data must have the same key and must keep it confidential. 

Symmetric cryptography is fast and efficient but can be vulnerable if the key is compromised.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/slide-09.png)
_Diagram showing how symmetric encryption works_

Asymmetric cryptography, also known as public-key cryptography, uses a pair of keys, one for encryption and another for decryption. The encryption key, known as the public key, can be widely distributed, while the decryption key, known as the private key, is kept confidential. 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/slide-10.png)
_Diagram showing how asymmetric encryption works_

Asymmetric cryptography is used for tasks such as digital signatures, key exchange, and data encryption, and is considered more secure than symmetric cryptography because the private key never needs to be transmitted or shared.

Hybrid cryptography is a combination of both symmetric and asymmetric cryptography. 

In a typical hybrid encryption scheme, the data is encrypted using a symmetric algorithm, and the symmetric key is then encrypted using an asymmetric algorithm and sent to the recipient along with the encrypted data. The recipient uses their private key to decrypt the symmetric key, and then uses the symmetric key to decrypt the data. 

Hybrid cryptography provides the security benefits of both symmetric and asymmetric cryptography, making it a commonly used encryption method.

## Public Key Infrastructure (PKI) 

PKI is a system for secure communication that uses a combination of public key cryptography, digital certificates, and certificate authorities (CAs) to authenticate the identity of parties involved in a communication and secure their communications.

Certificate Authorities (CAs) are organizations or entities that issue digital certificates, which are used to validate the identity of parties involved in a communication. 

CAs act as trusted third parties that verify the identity of parties and issue certificates attesting to that identity. The certificate includes information such as the identity of the owner, the public key of the owner, and the digital signature of the CA.

Trusted Root-CAs are the highest level CAs in the PKI hierarchy. They are responsible for issuing certificates for intermediate CAs, who in turn issue certificates for end entities, such as individuals or organizations. 

The trustworthiness of the entire PKI system is based on the trust in the root CAs. A trusted root CA is one that is widely recognized and trusted by users, systems, and applications. 

The trusted root CA's certificate is usually pre-installed in software and devices, such as web browsers, to facilitate secure communication and verify the authenticity of digital certificates issued by other CAs.

## Wrapping Up

With what you've learned here, you're now ready to use encryption tools like [VeraCrypt](https://www.veracrypt.fr/en/Home.html) and [GnuPG](https://gnupg.org/) to protect the data you store on your local machines. You'll be able to properly assess the safety and integrity of the online and cloud storage platforms where you store data remotely.

This article and the accompanying video are excerpted from [my Complete LPI Security Essentials Exam Study Guide course](https://www.udemy.com/course/complete-lpi-security-essentials-exam-study-guide/?referralCode=C2B6802EDB99578238B5). And there's much more technology goodness available at [bootstrap-it.com](https://bootstrap-it.com/)

