---
title: End-to-End Encryption – Is Your Data Safe from Big Tech?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-14T00:28:41.000Z'
originalURL: https://freecodecamp.org/news/end-to-end-encryption-is-your-data-safe
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/cyber-security-3400657__340.jpg
tags:
- name: encryption
  slug: encryption
- name: privacy
  slug: privacy
seo_title: null
seo_desc: "By Yehuda Clinton\nEvery now and then we hear buzzing in the news about\
  \ some egregious Big Tech privacy infringement. We are also frequently notified\
  \ about all the new steps our apps are taking to further protect our privacy. \n\
  Most of us then weigh th..."
---

By Yehuda Clinton

Every now and then we hear buzzing in the news about some egregious Big Tech privacy infringement. We are also frequently notified about all the new steps our apps are taking to further protect our privacy. 

Most of us then weigh the concerns and concede to the status quo without actually understanding the problem. As long as no one but us can see this message:

![Image](https://www.freecodecamp.org/news/content/images/2021/01/e2ee.jpeg)

Recently, WhatsApp announced that users must consent to sharing your data, including phone numbers and locations with Facebook. 

Let's start with the basic question:

## What information can apps, websites and operating systems have access to?

Let's try delving into WhatsApp as they have recently been under attack.

Every WhatsApp user encounters a statement like "this personal message has end-to-end encryption." Which means that WhatsApp or anyone else shouldn't be able to decipher this message once it leaves your phone. 

We should be able to trust that Facebook cannot read our WhatsApp messages on its server even if they store them until the recipient is connected. You can read WhatsApp's [privacy policy here](https://www.whatsapp.com/legal/privacy-policy).

**So far, no con game.**

What they don't mention in their privacy policy, however, is the in-app permissions about media and sensors. I'm referring to permission dialogs which pop up on first use.

I'm also referring to the data your OS shares with Facebook outside the app's ecosystem.

%[https://android.stackexchange.com/questions/71802/help-understanding-whatsapps-permissions]

While installing a new phone you could read this list of permissions accessed by the app including: Storage, location, Camera, Microphone, Accounts, Profile, Contacts and view apps running. 

The above _StackExchange_ article is over five years old and the list has changed since then. However you see a pattern of frequent changes to permissions and how difficult it can be to pin down when and how the app accesses media or device sensors.

### How does BIG-Tech use your data?

Let's go through some of the permissions listed for WhatsApp:

* **your social media profile** - details like 'phone number' and 'about'
* **location and time** - when you were at a given place
* **Photos/Media/Files** - hopefully they only use it for what they say
* **contacts** - they might share this within their ad algorithms 
* **camera** - hopefully it's only in use when in an encrypted video call
* **microphone** - hopefully... but see [this](https://www.quora.com/Can-Whatsapp-use-microphone-access-to-listen-to-converstations-even-when-not-being-used-for-audio-video-call-And-can-Facebook-use-that-data-to-shows-ads?share=1) and [this](https://www.quora.com/Is-Facebook-listening-to-me-through-my-phones-microphone). Sounds unclear
* **gyroscope/accelerometer** - determines when you're walking, sitting or driving
* **light sensor** - helps determine if your phone is in your pocket or against your head and so on

### So do they directly or indirectly use these sensors when you don't expect?

Facebook may not have to admit the answer to this, as google-play-services collects much of this information and shares it with them in different ways. Our best answer is that we can't really prove it one way or the other. 

It is all fine for most people if Big-Tech just uses our data to market relevant ads to us, but how can we know? Also if they aren't doing so today there's nothing stopping them from doing so one day.

### How they get away with it

We can see from other cases that large tech companies usually have each others' backs on these issues. Big-Tech has an established data-centric way of powering the online world. They don't seem to like competition. 

Note how the Parler app was booted from AWS and at the same time as being banned from the different app stores. There is plenty of other incitement happening on AWS hosted apps or Google. Even if there was ongoing pressure to dump Parler, being a growing social media app likely sealed their fate. 

## So what are the alternatives?

### [Telegram](https://telegram.org) & Signal

**Telegram** is a privacy focused instant messaging platform with some 500 million users. Although the app feels like top social networking its CEO [does not intend to monetize by utilizing user data](https://techcrunch.com/2020/12/23/telegram-to-launch-an-ad-platform-as-it-approaches-500-million-users/). 

Its mobile apps are open source so we can know exactly how it uses your phone data. This also allows us to assess the strength of the end-to-end encryption.

**Signal** is a completely open source messaging and calling service. Its non profit nature assures you that there's no ads or fees, but it's a bit more complicated to use and a lower quality service.

### How to keep your telegram private and secure

Use the settings to control who can see your photo, groups/channels or phone number. You can make your account name an alias and have your real name within your profile which can only be seen by your friends.

![Image](https://www.freecodecamp.org/news/content/images/2021/01/telegram.png)

## What you are trading for Privacy?

When using WhatsApp and similar social media, you're forced to adhere to the political and moral standards of Silicon Valley. As much as you may hate it, they do fairly well at protecting you from scams, harassment, and other criminal activities. 

If you decide to use an alternative, like Telegram, you should be ready to be your own filter. The Telegram or Signal apps may not be safe for children without careful supervision. There are [versions of the app available](https://www.mspy.com/telegram.html) which allow parents to monitor their children's messages and contacts. 

If you wish to learn more about underlying technologies we encounter daily, read [this book by David Clinton](https://bootstrap-it.com/davidclinton/keeping-up/).

If you are looking for encryption with your devices consider taking my [VPN course from Manning Publications](https://www.manning.com/liveproject/secure-business-infrastructure-with-a-custom-vpn?a_aid=bootstrap-it&a_bid=b9d7d398&chan=VPN).

