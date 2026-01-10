---
title: How Apple Pay Works Under the Hood
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-07T06:29:56.000Z'
originalURL: https://freecodecamp.org/news/how-apple-pay-works-under-the-hood-8c3978238324
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Zsr_ysZ5bNXXnzdC0LHY6w.jpeg
tags:
- name: Apple
  slug: apple
- name: iphone
  slug: iphone
- name: mobile
  slug: mobile
- name: Security
  slug: security
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Dumindu Buddhika

  Do you use Apple Pay? Have you ever wondered how an Apple Pay transaction goes through?
  In this post, you will learn how Apple Pay works end to end.

  Mobile payments have become very popular due to the convenience and the security
  ...'
---

By Dumindu Buddhika

Do you use Apple Pay? Have you ever wondered how an Apple Pay transaction goes through? In this post, you will learn how Apple Pay works end to end.

Mobile payments have become very popular due to the convenience and the security they offer. No more plastic cards to carry around, and you do not have to worry about losing them (what a relief!).

In this article, I am going to discuss how Apple Pay works in general and how it works when it is used at a physical POS terminal, specifically. I’ll briefly discuss the security benefits as well.

Before diving in, let’s get familiar with some basic terminology.

#### Secure Element

A secure element (SE) is something that is mentioned when talking about Apple Pay, so we need to understand what it is.

According to [Global Platform](https://www.globalplatform.org/mediaguideSE.asp):

> A Secure Element (SE) is a tamper-resistant platform (typically a one chip secure microcontroller) capable of securely hosting applications and their confidential and cryptographic data (e.g. key management) in accordance with the rules and security requirements set forth by a set of well-identified trusted authorities.

Apple Pay uses SE to store secret information associated with tokenized cards (we will talk about this later).

In the iPhones after iPhone 6, and in Apple Watch, an SE is embedded into the device’s near-field communication (NFC) chip. This is used at payment terminals to perform transactions over NFC. SE emulates a payment card during an Apple Pay transaction.

#### Tokenization

Tokenization as a process is being adopted more and more in the payments industry. Here we’ll try to understand the basics of Tokenization.

The following is a concise description from Wikipedia on Tokenization technology:

> **Tokenization**, when applied to data security, is the process of substituting a sensitive data element with a non-sensitive equivalent, referred to as a token, that has no extrinsic or exploitable meaning or value. The token is a reference (i.e. identifier) that maps back to the sensitive data through a tokenization system. The mapping from original data to a token uses methods which render tokens infeasible to reverse in the absence of the tokenization system

In the context of credit cards and Apple Pay, **tokenization** is used to replace the Primary Account Number (PAN, or the credit card number) with a token. A token looks like a normal credit card number, but it’s not the original PAN. Tokenization stops the original card number from being used during transactions.

Tokens have no meaning by themselves and are worthless to criminals if a token is stolen. There is no algorithm to derive the Primary Account Number if you have a token. This makes it impossible for criminals to reverse engineer the Primary Account Number from a token.

Click [here](https://en.wikipedia.org/wiki/Tokenization) for the Wikipedia article on tokenization if you want to learn more.

The following diagram describes the transaction flow of Apple Pay. We will discuss these step by step in the coming sections.

![Image](https://cdn-media-1.freecodecamp.org/images/Tvs9gM2jDlgnFkUqWnw7f7bE1YG4DsYEsJah)
_ymedialabs.com_

### Adding a Card to Apple Pay

![Image](https://cdn-media-1.freecodecamp.org/images/C4FQQR5WKo8KpyiLxfG3tvmsLRwiaOv6h5ny)
_[http://www.iphoneincanada.ca](http://www.iphoneincanada.ca" rel="noopener" target="_blank" title=")_

A card can be added to Apple Pay by either scanning the card or by submitting the card information. Then this information is submitted to Apple servers.

Apple sends the received card information to the relevant card network (Visa, MasterCard, AmericanExpress, Discover, and so on). Then the card network validates the card information with the issuing bank.

After the validation, the card network acting as a [TSP](https://www.slideshare.net/bellidcom/what-is-a-token-service-provider-52887269) (Token Service Provider) creates a token (which is called a DAN or a Device Account Number in the context of Apple Pay) and a token key. This DAN is generated using tokenization and is not the actual card number.

Afterward, this information is sent back to Apple servers. After the device receives this information from Apple servers, it is saved in the device’s secure element (SE).

### Initiating a Transaction Using Apple Pay

![Image](https://cdn-media-1.freecodecamp.org/images/fzP2zrOr4FBQoNSAervf20OXqrWoeIHJhZHi)
_support.apple.com_

When you use your Apple device at a POS terminal to make a payment, the device communicates with the terminal to initiate a transaction. Apple Pay uses EMVCO’s [contactless specification](https://www.emvco.com/emv-technologies/contactless/) to communicate with the terminal. If the terminal does not support EMV contactless, Apple Pay falls back to use contactless MSD (magnetic stripe data) mode.

#### EMV Contactless mode

When EMV contactless mode is used, the Apple device communicates with the terminal according to the EMV contactless [specification](https://www.emvco.com/emv-technologies/contactless/). The secure element on the device generates a **dynamic cryptogram** for each transaction using the token, token key, amount, and other information related to the transaction. This dynamic cryptogram is then sent to the payment processor along with the token (DAN), transaction amount, and other required information to process the transaction.

#### Contactless MSD mode

Contactless MSD exists to support terminals which are still not able to process using EMV contactless mode. Most of the terminals are still operating using contactless MSD mode. Let’s take a deeper look at how a transaction goes through using contactless MSD mode.

MSD, or Magnetic Stripe Data, is how older cards store card details. Data is stored as **tracks** in magnetic stripe cards. Magnetic stripe cards can have up to 3 tracks, and each track (track1, track2, track3) has a different format. Please click [here](https://en.wikipedia.org/wiki/ISO/IEC_7813) for additional information on track data.

In Apple Pay contactless MSD mode, the track2 data format is used to transfer the card data to the payment processor which then communicates with the card network.

Let’s take a look at some example track data sent from a terminal to the processor for an Apple Pay transaction.

370295292756481=220672716078290600047

![Image](https://cdn-media-1.freecodecamp.org/images/06Uue0GUDG01OBeKpoIeOHee0WRnfRdPm-mP)

Above is an example of track data received from a terminal which was captured at a payment gateway.

Let’s understand this data segment by segment,

* Highlighted in yellow - This is the Device Account Number or the DAN (The example DAN here is from an AmericanExpress card. You can validate the bank identification number (BIN), or initial 6 digits in the credit card number, [here](https://www.bincodes.com/bin-checker/)).
* Highlighted in blue - This is the credit card expiry year and month(yy/mm)
* Highlighted in pink - This is the service code. Click [here](https://atlassian.idtechproducts.com/confluence/display/KB/Credit+Card+Service+Code+Chart++) to understand more about this.
* Highlighted in purple - This part of data is discretionary to the card network. In case of Apple Pay, this is used as a **dynamic card verification value (CVV).**

We learned that in the EMV mode a **dynamic cryptogram** is generated. Here the **dynamic CVV** plays the role of the cryptogram. This is generated using the token key and other transaction-related data (similar to the generation of a **dynamic cryptogram**).

The track data shown above is sent to the [acquirer](https://en.wikipedia.org/wiki/Acquiring_bank) along with the transaction amount. The acquirer forwards this information to the relevant card network (Visa, MasterCard, and so on ) based on the [BIN](https://www.investopedia.com/terms/b/bank-identification-number.asp).

### Completion of an Apple Pay Transaction

When the card network receives the transaction request, it identifies whether it’s an actual card number or a tokenized card number. If it is tokenized (which is the case for Apple Pay transactions), the card network validates the cryptogram (or dynamic CVV) using their copy of the **token key** (the card network is acting as a [TSP](https://www.slideshare.net/bellidcom/what-is-a-token-service-provider-52887269) here).

After some other additional validations, the card network de-tokenizes the DAN and obtains the original PAN (primary account number).

This transaction request is sent to the [issuer](https://www.thebalance.com/credit-card-issuer-959984) (the bank or the financial institution who issued the credit card) along with the original PAN. The issuer authorizes the transaction and sends back the response which eventually reaches the POS terminal.

Yay! Transaction complete!

![Image](https://cdn-media-1.freecodecamp.org/images/QLw4aphNtbO5blklWMB-m9S2UsU5XWY7d63z)
_support.apple.com_

### Replaying Transaction Requests

One of the biggest problems with the traditional card transactions is the ability to replay past transaction requests ([replay attack](https://en.wikipedia.org/wiki/Replay_attack)). If you resend the same transaction request, another transaction would be done with the same data.

With Apple Pay, this does not happen (also when using EMV cards directly on the terminal as well). Every transaction request can only be used once. The dynamic cryptogram (dynamic CVV in MSD mode) ensures this. For each transaction, a new cryptogram is generated which can only be used once (and is only valid for a certain time period).

### Conclusion

In this article, we have gone through an overview of the Apple Pay transaction flow. I will discuss Google Pay in a coming article.

#### References

* [http://www.gmarwaha.com/blog/2015/01/03/apple-pay-an-attempt-to-demystify-take-2/](http://www.gmarwaha.com/blog/2015/01/03/apple-pay-an-attempt-to-demystify-take-2/)
* [https://www.emvco.com/emv-technologies/contactless/](https://www.emvco.com/emv-technologies/contactless/)
* [http://msrtron.com/blog-headlines/blog-card-data](http://msrtron.com/blog-headlines/blog-card-data)
* [https://www.slideshare.net/bellidcom/what-is-a-token-service-provider-52887269](https://www.slideshare.net/bellidcom/what-is-a-token-service-provider-52887269)

#### Before you go!

If you have enjoyed this article, claps are welcome!

