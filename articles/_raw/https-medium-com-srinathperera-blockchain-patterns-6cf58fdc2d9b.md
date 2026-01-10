---
title: Four architecture pattern candidates for Blockchain-based decentralized applications
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-23T15:49:36.000Z'
originalURL: https://freecodecamp.org/news/https-medium-com-srinathperera-blockchain-patterns-6cf58fdc2d9b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*iCv3PnwJ3jvu2pDhEq3ZhQ.png
tags:
- name: Bitcoin
  slug: bitcoin
- name: Blockchain
  slug: blockchain
- name: Cryptocurrency
  slug: cryptocurrency
- name: software architecture
  slug: software-architecture
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Srinath Perera

  Blockchain has a diverse set of use cases, ranging from finance to a decentralized
  Internet. However, most blockchain use cases can be implemented using relatively
  few patterns. For example, A Pattern Collection for Blockchain-based...'
---

By Srinath Perera

Blockchain has a diverse set of use cases, ranging from finance to a decentralized Internet. However, most blockchain use cases can be implemented using relatively few patterns. For example, [A Pattern Collection for Blockchain-based Applications](https://www.researchgate.net/publication/325439030_A_Pattern_Collection_for_Blockchain-based_Applications) provides a list of 15 Blockchain patterns.

Fine-grained patterns, such as described above, are useful. However, system design needs a much higher level of abstractions. It is useful also to have more coarse-grained macro patterns, which we call architecture patterns. This post describes four such architecture patterns.

Let’s get started. To describe patterns, I will use the template described in by Aleksandra Tešanovic in [What is a Pattern](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.123.1162&rep=rep1&type=pdf)?

### Architecture Pattern for IAM.

**Context:** IAM environments include many users and service providers. IAM systems give each user an account and set of capabilities enabling users to go to service providers, demonstrate their ownership of accounts, and then receive services based on their capabilities.

**Forces:** Need to implement a decentralized IAM environment where a single rogue user or few users can’t significantly affect the system.

**Solution:** Proposed pattern candidate uses World Wide Web Consortium (W3C) DID specification and W3C Verifiable Claims specification in the following manner.

![Image](https://cdn-media-1.freecodecamp.org/images/lUMFQa8e5GZRqE9PVExbKKUBq43VTd0LCauy)
_Figure 1: Blockchain-based IAM Architecture Pattern_

Let’s assume Alice needs an identity (DID, which is a unique identifier). As shown by the figure for creating a new DID, Alice creates an entry in the blockchain. This entry includes a randomly generated identifier, a link to the repository with her profile data, and a hash of the profile data. The user profile contains a public key and a set of verifiable claims. The generated random identifier now becomes Alice’s DID because only she owns the private key that corresponds to the public key.

Verifiable claims are delegation tokens signed by a competent authority. The creator also records them in a blockchain together with the hash of the claim in a manner similar to the DID.

Alice obtains the verifiable claims in the first place by going to authorities. For example, the department of personal registration or equivalent is the proper authority for verifiable claims of name, address, and date of birth. Assuming authorities issue verifiable claims, Alice first demonstrates her ownership of the DID uses a challenge-response-protocol. Then she submits requests for verifiable claims for her attributes, which may, for example, include her name, address, degree, and date of birth. To update her profile data, Alice will add a new entry to the blockchain with a new hash of the profile.

In the challenge-response-protocol, the validator generates a random seed, encrypts it using Alice’s public key, and then challenges Alice to demonstrate that she has the private key by decrypting the encrypted seed. Since Alice has the private key, she must be the owner of the DID.

A different user or an organization (authenticator), Bob, who wants to identify Alice, first receives the DID from Alice, read all entries related to that DID from the blockchain, retrieve Alice’s profile data, and verify them. Bob can verify the identity of Alice (identification) again using challenge-response-protocol. Then Bob can confirm the verifiable claims and be assured that the claims about Alice are true.

We can layer most IAM use cases on top of this architecture pattern. For example, we can achieve access control either by issuing verifiable claims for actions we want users to perform or by only accepting users who have certain properties (e.g., age, job description, group membership) in their verifiable claims. An implementation may choose to cache relevant subsets of the profile data in a database to improve performance.

### Architecture Pattern for Auditable History or Workspace

**Context:** A two or more parties perform transactions or works together, and their activities need to be recorded in an indisputable manner.

**Forces:** Need to implement a decentralized audit log or a workspace where a single rogue user or few users can’t significantly affect the system.

**Solution:** The proposed system records activities and creates entries in the blockchain for those records. The entry contains the hash of activity records, and therefore, the records can’t be disputed later.

![Image](https://cdn-media-1.freecodecamp.org/images/iF-qjFAl8ERHYc8MkajFeVnIUK10RiWz2RVG)
_Figure 2: Blockchain based Auditable History or Workspace Architecture Pattern_

For example, let’s assume Alice wants to pay a tax. Tax Server accepts the payment application, creates a digital receipt, records its hash in the blockchain, and sends the receipt to Alice. Alice can verify the receipt by calculating the hash and checking against the value stored in the blockchain. After this, Bob can’t deny the receipt because the receipt hash and time are recorded in the blockchain.

If the activities are numerous, there may be a need to workaround blockchain performance limitations. Therefore, some implementations may record a hash of several activity records as a block instead of a single activity record.

### Architecture Pattern for Registry or Marketplace

**Context:** A registry is a collection of data entries that can be searched and retrieved over the network. A market place is a registry that allows users to buy the services or products represented by data entries. For example, a registry may be a catalog of available APIs.

**Forces:** Need to implement a decentralized environment where a single rogue user or few users can’t significantly affect the system.

**Solution:** The proposed pattern works as follows.

![Image](https://cdn-media-1.freecodecamp.org/images/PxrO0b03JFpQ-JuWXHXtzkfq56xJHND3gesV)
_Figure 3: Blockchain based Registry Architecture Pattern_

Let’s first consider a registry. With the proposed architecture, when a user issues a registry update (to add or modify an entry), the client records the change in the blockchain. If data in the update is large, the blockchain record may contain a link to the data and a hash value of the data. If data stored in the registry needs to be amended, the registry client adds a new record to the blockchain with amended information.

In the diagram above, each user has a registry client running in the local machine (e.g., laptop or phone). Each registry client reads the update records from the blockchain, verifies the update data against the hash included in the records, and reconstructs the most current view of records from updates. For example, by reading blockchain records about APIs, their additions, amendments, and removals, the registry client can create a view that shows current APIs included in the registry. To avoid having to read and verify all records every time the registry is used, clients might store data in a database and index it. The client should periodically check the blockchain and update the registry.

Blockchain works well as a “service marketplace,” since the same service may be sold many times. However, due to performance limitations, blockchain-based marketplaces are not suitable for items that can be sold only once.

To illustrate, the functionality of a blockchain-based registry, let’s look at when Alice wants to subscribe to “weather news service” in the blockchain marketplace. When she submits her request, the registry creates credentials for the service and shares it with Alice. The payment may happen in one of several ways: using Bitcoins, via a smart contract where payments are made on a timely basis, or by some out-of-bound means.

### Architecture Pattern for Smart Contracts and Managed Things

Under this pattern, we consider two cases. First, we consider smart contracts, and as the second, we consider a common special case of smart contracts: “Managed Things.”

#### Smart Contracts Pattern

**Context:** Multiple users want to abide by a contract, described as an executable program. Contract undergoes state transitions as per conditions defined in the contract, and at a given time, everyone can agree on the current status of the contract.

**Forces:** need to implement an environment where a single rogue user or few users can’t significantly affect the system.

**Solution:** Smart contacts are part of blockchain technologies and supported by blockchain implementations, such as Ethereum. A contract is described using a smart contract language and distributed to all participants. As conditions defined in the contract changes, each participant executes the contract and records the current status in the blockchain using the consensus algorithm.

#### Managed Things Pattern

**Context:** We need to track the ownership of real-world smart things. Here smart things are real-world objects that are capable of running computing logic within them. The owner is allowed to control and perform actions on the real world things. Also, the owner may transfer his ownership to someone else.

**Forces:** need to implement an environment where a single rogue user or few users can’t significantly affect the system.

**Solution:** Following describes the implementation of the pattern using Car as the managed thing as an example.

![Image](https://cdn-media-1.freecodecamp.org/images/8je7rRiQV0zVRuuvCXjnHJHMNlnNjOrv29r4)
_Figure 4: Blockchain based Managed Things Architecture Pattern_

We can implement a blockchain for a managed thing, in this case, a car, in two steps. First, the manufacturer records the DID and the public key of the owner of the car. When ownership changes, the owner adds a new record in the blockchain specifying the new owner. Second, when checking for ownership, the car first retrieves all records in the blockchain and verifies that each record is added by the owner at that time. This is done by checking the public key of the user who wrote the record against the public key included in the previous ownership record. The last owner in this valid chain is the current owner.

After determining the owner, the car logs in the current owner, Alice, by retrieving her public key and carrying out a challenge-response-protocol-based login with Alice’s phone, which has Alice’s private key.

Such a system reduces the risks associated with remotely controlled artifacts. For example, in a non-blockchain implementation, someone with access can change the ownership of your car. However, with the blockchain-based model, to remotely control the car, a would-be attacker must change the ownership record in the blockchain, which is very hard to achieve without being the owner.

However, it is hard to stop someone who has access to the “thing” from physically changing the logic running inside (e.g., by replacing the firmware of the car). One solution to this problem is to build some form of self-destruct that triggers when tampering into the artifact is detected.

For example, Alice buys the car from Bob using a smart contract that pays Bob and updates the ownership of the vehicle. After the transaction, Alice walks to the car, which reads Alice’s DID from the phone, retrieves her public key, authenticates her using a challenge-response-protocol by communicating with the phone that has Alice’s private key, verifies her ownership, and unlocks the car.

### Conclusion

We discussed four blockchain based architecture patterns. The GitHub document, [Blockchain-based Integration Use Cases](https://github.com/wso2/ETAC/blob/master/blockchain/blockchain-usecases.md), shows these patterns in action, describing how 30-plus blockchain use cases can be implemented using these four patterns.

If you have opinions about the above patterns or know about other patterns, I would really like to hear about them.

I hope this was useful. If you like this, you might also like a detailed blockchain analysis in our recently published paper, “[A use case centric survey of Blockchain: status quo and future directions](https://peerj.com/preprints/27529/).”

