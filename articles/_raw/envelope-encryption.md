---
title: How to Manage Encryption at Scale with Envelope Encryption & Key Management
  Systems
subtitle: ''
author: Rohit Jacob Mathew
co_authors: []
series: null
date: '2021-10-27T22:52:59.000Z'
originalURL: https://freecodecamp.org/news/envelope-encryption
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/1400-x-600.jpg
tags:
- name: Application Security
  slug: application-security
- name: encryption
  slug: encryption
seo_title: null
seo_desc: "Recently at work, I came across an interesting method to handle encryption\
  \ at scale called envelope encryption. \nFirst of all, it increases security and\
  \ helps you ease out the management of encryption keys. But it's also a highly recommended\
  \ pattern ..."
---

Recently at work, I came across an interesting method to handle encryption at scale called envelope encryption. 

First of all, it increases security and helps you ease out the management of encryption keys. But it's also a highly recommended pattern by PCI-DSS (Security Standard for Credit Card Processing) and results in much stronger data privacy and data protection of Personally Identifiable Information (PII). 

When we think of data, there are 3 places we can think of encrypting it:

* At Rest – on hardware storage devices like a disk or in your devices
* In Transit – while moving data between different locations like server to server through API calls
* In Use – while it's being used by a server (this is a new concept and is still being researched)

We will be dealing primarily with encryption at rest, and envelope encryption is a popular pattern for this use case.

## So What is Envelope Encryption? 🤔

Envelope encryption involves encrypting your data with a Data Encryption Key, then encrypting the Data Encryption Key (DEK) with a Customer Master Key (CMK). 

You then store both the encrypted data and the encrypted DEK alongside each other in the database. This practice of using a wrapping key to encrypt data keys is known as envelope encryption.

You need to understand these two keys before we see how the encryption process takes place:

1. Customer Master Key (CMK)
2. Data Encryption Key (DEK)

### Customer Master Keys/Root Keys/Key Encryption Keys (CMK)

These are symmetric keys used to encrypt, decrypt, and re-encrypt data. They can also generate Data Encryption Keys that you can use outside of the KMS system. They follow the below rules:

* Access to these keys must be restricted to the least endpoints
* Access to these keys should be secured through ACL
* These keys must be stored in a location that is secure like a KMS of a Hardware Security Module (to comply with [FIPS 140-2](https://en.wikipedia.org/wiki/FIPS_140-2))

In systems like Google Cloud Key Management Service, you have a hierarchy of keys as seen below (you can find more information [here](https://cloud.google.com/security/encryption/default-encryption#encryption_key_hierarchy_and_root_of_trust)):

![Encryption Key Hierarchy at Google](https://cdn.hashnode.com/res/hashnode/image/upload/v1635198625726/DgTfDZpGk.png)

### Data Encryption Keys (DEK)

Data keys are encryption keys you can use to encrypt data, including large amounts of data and other data encryption keys. 

Unlike CMK's, which can't be downloaded, data keys are returned to you for use outside of the KMS. Some of the best practices for DEKs are as follows:

* You should generate DEKs locally
* When stored, always ensure DEKs are encrypted at rest
* For easy access, store the DEK near the data that it encrypts
* Generate a new DEK every time you write the data. This means you don't need to rotate the DEKs.
* Do not use the same DEK to encrypt data from two different users
* Use a strong algorithm such as 256-bit Advanced Encryption Standard (AES)

## Envelope Encryption Process

First, an API request is sent to KMS to generate Data key using CMK.

Then the KMS returns a response with Plain Data key and Encrypted Data key (using CMK).

![Generate Data Keys](https://cdn.hashnode.com/res/hashnode/image/upload/v1635198711784/Bm05yko4g.png)

Data is encrypted using the Plain Data key, and then the Plain Data key is removed from memory.

![Encryption Process](https://cdn.hashnode.com/res/hashnode/image/upload/v1635198735343/vjqUrCTa1.png)

The Encrypted Data and Encrypted Data Key are packaged together as an envelope and stored.

![Encryption Process With Data Stored at Rest](https://cdn.hashnode.com/res/hashnode/image/upload/v1635198756845/mXf8rwGhU.png)

## Decryption Process

First, the Encrypted Data key is extracted from the envelope.

Then an API request is sent to KMS using Encrypted Data key which has information about CMK to be used in KMS for decryption.

The KMS returns a response with the Plain Data Key.

![Getting Plaintext Data Key](https://cdn.hashnode.com/res/hashnode/image/upload/v1635198816460/dl8Q5RoPKew.png)

Then the Encrypted Data is decrypted using the Plain Data key, and the Plain Data Key is removed from memory.

## **How is Envelope Encryption Different From Other Encryption Patterns**? 🤔

Every service you build requires encryption at some point. This could be passwords or PII in a database, credentials for an external service, or even files in a filesystem.

### Configuration Files

You can easily handle some of these situations with a configuration file but they pose their own security risks like:

* Proper planning is needed to keep the data secure
* Multiple formats are present, like YAML, JSON and XML to name a few
* Exact storage locations may be hard-coded in the app, making deployment potentially problematic
* Parsing of the config files can be problematic.

### Symmetric Encryption

You can encrypt data using a symmetric key but they suffer from a major issue which is Key Management.

You need to find a way to get the key to the party with whom you are sharing data. But if someone gets their hands on a symmetric key, they can decrypt everything encrypted with that key.

### Asymmetric Encryption

You can encrypt data using Asymmetric Encryption which is considered a standard now a days. However, some of its cons are:

* It is a slow process which makes its not suitable for decrypting bulk messages
* When you lose your private key, your received messages will not be decrypted
* If your private key is identified by an attacker, they can read all of your messages 

### Envelope Encryption

Some of the benefits offered by envelope encryption are:

* **A combination of benefits from symmetric and asymmetric encryption** – The data is encrypted using a DEK which follows symmetric encryption. The DEK is encrypted by a CMK which follows asymmetric encryption. By using asymmetric encryption, encrypted DEKs can be shared and unencrypted only by those with access to the CMK, mitigating the key exchange problem of symmetric algorithms.
* **Easier key management** – Multiple DEKs can be encrypted under a singular root key and ease the management of keys in a KMS. You can also do more secure key maintenance by rotating your root keys, instead of rotating and re-encrypting all of your DEKs.
* **Data key protection** – Because we encrypt the data key with the CMK, we don't have to worry about storing the encrypted data key. Thus, we can safely store the encrypted data key alongside the encrypted data.

## Why Key Management Systems Work Well at Scale 

Envelope Encryption and KMSs working so well at scale because of **Performance.** Like we mentioned before, Asymmetric Encryptions are typically slow and Symmetric Encryptions are very fast but managing keys can be an issue. 

So in Envelope Encryption, for a large quantity of data, you quickly encrypt it using symmetric encryption with a random key. Then just the key is encrypted using asymmetric encryption. This gives the benefits of asymmetric encryption, with the performance of symmetric encryption.

![KMS Used at Scale in Google](https://cdn.hashnode.com/res/hashnode/image/upload/v1635198563732/1E9VcEqZ-.png)

Key Management Systems like AWS KMS, Azure Key Vault, and Google Cloud Key Management Service gives you a fully managed service to store and manage encryption keys. These use envelope encryption internally, and they’re used by default in a lot of services that support encryption in cloud infrastructure providers like AWS, GCP, Azure, and others.

An ideal key management system should be highly available, it should control access to the master key(s), it should audit the key(s) usage, and finally, it should manage key(s) lifecycle.

Thus by having the above characteristics and by using envelope encryption internally, Key Management Systems are ideal to handle encryption at scale.

## Summary

Envelope Encryption is one of the most trusted application security design patterns used at scale. It is the default encryption method used in services like AWS S3, GCP, and others. 

Hopefully, this helps you understand how you can encrypt/decrypt a large amount of data using the envelope encryption method at scale in a more trusted setup.

Thanks for reading! I really hope that you find this article useful. I'm always interested to know your thoughts and am happy to answer any questions you might have. If you think this post was useful, please share it so others can read it, too.

P.S. – Do feel free to connect with me on [LinkedIn](https://www.linkedin.com/in/rohitjmathew) or [Twitter](https://twitter.com/iamrohitjmathew).

## Resources

This article leans heavily on the following material:

* [Google Cloud Data Encryption - Jayendra's Cloud Certification Blog -](https://jayendrapatil.com/tag/envelope-encryption/)
* [AWS KMS concepts - AWS](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html)
* [AWS KMS and Envelope Encryption - Manish Pandit](https://lobster1234.github.io/2017/09/29/aws-kms-envelope-encryption/)
* [Cloud Architecture Pattern: Envelope Encryption (or Digital Envelope) with Public Cloud Providers Part 1 - Nilay Parikh](https://blog.nilayparikh.com/security/application/cloud-architecture-patterns-envelope-encryption-or-digital-envelope-with-public-cloud-providers-part-1/)
* [AWS KMS Envelope Encryption - Chirag Modi](https://dev.to/chiragdm/aws-kms-envelope-encryption-3689)
* [Protecting data with envelope encryption - IBM](https://cloud.ibm.com/docs/key-protect?topic=key-protect-envelope-encryption)
* [Envelope encryption - GCP](https://cloud.google.com/kms/docs/envelope-encryption)
* [Encryption at rest in Google Cloud - GCP](https://cloud.google.com/security/encryption/default-encryption)

%[https://youtu.be/StJ1NOQjAjo]


