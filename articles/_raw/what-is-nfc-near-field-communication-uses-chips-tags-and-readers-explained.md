---
title: What is NFC? Near Field Communication Uses, Chips, Tags, and Readers Explained
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2020-11-03T18:00:12.000Z'
originalURL: https://freecodecamp.org/news/what-is-nfc-near-field-communication-uses-chips-tags-and-readers-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9581740569d1a4ca0d5c.jpg
tags:
- name: finance
  slug: finance
- name: fintech
  slug: fintech
- name: payments
  slug: payments
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'NFC is everywhere these days. You''ve probably seen it in your phone settings,
  or heard about it online.

  While the use of NFC for things like contactless payments was growing steadily,
  it exploded early this year due to the Coronavirus pandemic.

  In th...'
---

NFC is everywhere these days. You've probably seen it in your phone settings, or heard about it online.

While the use of NFC for things like contactless payments was growing steadily, it exploded early this year due to the Coronavirus pandemic.

In this article we'll go over what NFC is, what it's used for, some creative ways to use NFC, and more.

## What is NFC and how does it work?

NFC stands for near-field communication. It is a standard for devices to communicate with each other wirelessly from a very close distance.

NFC is a subset of another technology called RFID, so let's dig a bit into that before circling back to NFC.

### What is RFID?

Radio-frequency identification, or RFID, is a generic term for technologies that use radio waves from a reader to track specific tags. These tags all include an antenna and a tiny chip, and can come in many shapes and sizes. 

Highway toll payment devices and those plastic things on clothes and other expensive items in stores are some common examples of RFID tags.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-123.png)
_A diagram of an RFID tag. NFC tags look very similar – [Source](https://www.analogictips.com/rfid-tag-and-reader-antennas/)_

If you've ever seen those big devices on either side of a store entrance, those are just big RFID readers. They're constantly transmitting radio waves and listening for a response.

So what happens if you try to leave a store and there's still a tag on the item you bought? 

Most RFID tags are unpowered, so when the antenna in the tag picks up radio waves from the reader, it generates a small amount of electricity. That electricity activates the chip inside the tag, and it sends a signal with the information stored on the chip back to the reader. 

In this case, when the reader receives a signal back from the tag on your item, it sounds an alarm.

### How are RFID and NFC related?

NFC is a newer, high-frequency version of RFID, and also involves both tags and readers. 

NFC's higher frequency means that, while it can transfer data much faster than RFID, it only works from a distance of about 4 cm/1.6 in or less. Meanwhile, RFID works from a distance of up to 12 m/40 ft.

## What is NFC used for?

There are a lot of use cases for NFC, but here are some of the most common you'll see.

### Contactless payments

These days, the most common thing that NFC is used for is contactless payment. Many newer credit and debit cards include an NFC tag, so you can just hold your card just above a payment terminal rather than swipe or insert it.

Contactless payment enabled credit and debit cards have a symbol on them similar to these:

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-124.png)
_Most contactless payment cards will have a similar symbol on the front or back – [Source](https://www.emvco.com/emv_insights_post/contactless-payments-how-emvco-supports-seamless-and-secure-acceptance/)_

Most modern phones include an NFC chip, which can act as both an NFC reader/writer and tag. 

This chip, paired with a mobile payment app like Google Pay, Apple Pay, and Samsung Pay, means that you might not even need to take your wallet out anymore. 

Instead, your phone can act as a virtual NFC tag for your credit or debit card, even if said card doesn't have an actual NFC tag inside it.

Whether you use your contactless card or a mobile payment app, every payment you make involves tokenization for extra security.

Tokenization is when your card's information is used to generate a random, temporary token for each transaction. Then, your card or mobile payment app can send that temporary token safely, rather than transmit your actual card number, name, and other sensitive information.

However you choose to pay, using a contactless payment card, a mobile payment app, or inserting your card's chip are all [much safer than the old method of swiping](https://www.engadget.com/2019-08-29-how-to-make-online-payments-safely-and-securely.html).

### Interacting with products

Traditionally RFID is used for tracking inventory in warehouses and stores. But once a product leaves the store, its RFID tag is disabled.

A lot of products now include NFC tags for additional interaction after you leave the store. Nintendo's Amiibo figures are probably the most common recent example of this:

![Image](https://www.freecodecamp.org/news/content/images/2020/10/image-96.png)
_If this isn't the cutest NFC tag, I don't know what is – [Source](https://www.nintendo.com/amiibo/detail/detective-pikachu-amiibo/)_

When you scan an Amiibo figure with your Nintendo console, you can get special characters, items, or other additional content, depending on the game and figure you use.

Your Nintendo console can also write information back to the NFC tag in your figure, again, depending on the game and figure.

Other companies like Nike have been including NFC tags in things like sports jerseys and sneakers. This allows you to get personalized content based on the product you scan (recent scores for a team, stats for a specific player, and so on), or even check that a product is genuine.

### Data transfer

Unlike RFID, which is typically one-way communication between a reader and a tag, NFC allows for two-way communication.

Some phones are able to use NFC to transfer data like contacts or photos between two devices if you touch them together.

## Creative uses for NFC

One of the coolest things you can do with NFC is buy a pack of tags online and program them to do different things with your phone.

For example, if you're tired of always giving your WiFi password out to guests, you could program an NFC tag to automatically connect to your network. Then, all your guests need to do is make sure NFC is enabled and hold their phones near the tag.

You could also program NFC tags to control different smart devices around your house. You could have a tag that toggles a smart lamp on or off, or one that sets the thermostat. 

The commands triggered by the NFC tags can also be personalized to specific devices. For example, if you like the room a bit cooler than your partner, when you scan the thermostat tag it can lower the temperature. But when your partner scans it, it could raise the temperature to their preferred setting.

There are a lot of other interesting ways to use NFC tags to make your life just a little bit easier. Check out this video for more ideas and to see how to program your own NFC tags in both iOS and Android:

%[https://www.youtube.com/watch?v=o9WHrX9cvXA&t=87s]

## In summary

Though you might not have heard much about NFC until earlier this year (I certainly hadn't), it will likely become the standard we pay for things. 

And considering all the cool stuff you can do with a phone and a pack of NFC tags, it's surprising that NFC isn't more widely adopted.

If you end up programming your own NFC tags, let me know what you did and how you did it over on [Twitter](https://twitter.com/kriskoishigawa).

