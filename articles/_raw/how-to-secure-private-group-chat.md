---
title: How to Set Up an Extremely Secure Private Group Chat
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2020-01-15T20:20:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-secure-private-group-chat
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/WinonaSavingsBankVault.JPG
tags:
- name: information security
  slug: information-security
- name: privacy
  slug: privacy
- name: Security
  slug: security
seo_title: null
seo_desc: 'Chat room tools like Discord and Slack are more popular than ever. But
  they were never intended as a place for sensitive discussions or secure file sharing.

  Discord was built primarily for voice chat during online games. And Slack''s roots
  are in corp...'
---

Chat room tools like Discord and Slack are more popular than ever. But they were never intended as a place for sensitive discussions or secure file sharing.

Discord was built primarily for voice chat during online games. And Slack's roots are in corporate communication.

Neither of these chat tools were designed with privacy at their core.

Another de-facto chat tool a lot of people use - Twitter - was designed for quick, public status updates. They tacked on Direct Messages, but these aren't particularly private, either.

According to [PrivacySpy](https://privacyspy.org/directory/) – a website that analyzes the privacy policies of big tech companies – neither of these three options may be private enough for you.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Directory___PrivacySpy.jpg)

According to their privacy policies, Discord, Slack, and Twitter may all be willing to turn over your data to someone else without even requiring a subpoena or a court order.

There could be situations where the government – or even a private corporation – could gain access to your messages. They might even make them public.

If this possibility bothers you, fear not. If you really want to be able to talk with friends without risk of your group being compromised or your secrets getting out, there are plenty of options at your disposal.

This article will show you several ways of creating group chats where no company has the power to hand your conversations over to anyone.

# How to Chat Securely Using Messaging Apps

First, there are messaging tools designed by security experts.

You may hear Mark Zuckerberg talk about how WhatsApp and Facebook Messenger use encryption. Or Tim Cook talk about how iMessage uses encryption.

All three of these messaging tools are closed-source, so it's hard to know how securely they're encrypting your messages, and who inside (and outside) the company can access them.

That means these are not sufficiently private tools for sensitive conversations.

There are truly private messaging tools that are open source, though. Which gives them additional accountability.

# Using Signal Private Messenger to Chat Securely

![Image](https://www.freecodecamp.org/news/content/images/2020/01/signal.jpg)
_Signal Private Messenger in the Google Play Store_

[Signal Private Messenger](https://signal.org/download/) has end-to-end encryption and uses verification numbers.

Signal also offers disappearing messages, encrypted phone calls, and a whole lot of other secure communication features. And to the topic at hand, Signal offers group chat.

Signal is free and works on iOS, Android, and on your desktop. I've used it for several years.

The main downside to Signal is that you need to download an app and associate your account with your phone number. This is not an anonymous communication tool. If you were - say - a journalist meeting with sources - you might need to find a more secure option.

# Using Keybase to Chat Securely

![Image](https://www.freecodecamp.org/news/content/images/2020/01/The_App_-_Install_Macos___Keybase_Docs.jpg)
_A screenshot from Keybase_

Another messaging tool is [Keybase](https://keybase.io/download). This is a file-sharing tool that also has secure chat built into it.

Unlike Signal, Keybase does store your encrypted messages on their server, so in theory it is less secure. But it is open source, and the encryption they use would in theory cost billions of dollars worth of supercomputer time in order to crack with today's technology.

Keybase also requires installing software and proving your identity - most commonly through making public posts from your social media accounts.

# But if you really, really want your group chat to be private without installing apps...

I'm going to lay out the tools I would use if I wanted to form a group around a sensitive topic, or from inside a country with an authoritarian regime.

And a word of warning - we're going to get into some real spy thriller stuff here. Nothing as elaborate as [communicating through crossword puzzles in daily newspapers](https://en.wikipedia.org/wiki/D-Day_Daily_Telegraph_crossword_security_alarm), but similarly esoteric.

# How to Create Your Private Chat Room

If you just want to be able to chat securely without a lot of set-up time, this is the most secure chat room tool I know of: [LeapChat](https://www.leapchat.org).

This bare-bones chat room uses end-to-end encryption. It encrypts messages both in transit and at rest. And it decodes the messages when they reach your browser.

There is no need to sign in using an email address or phone number - or to even remember a password. If you know the room's URL, you can just choose a username and start chatting.

But the only way to know a LeapChat room's URL is to get it from someone else. You aren't going to guess it. Because the URLs are 25 English-language words long, and each of these words come from the EFF list of 7,776 words. That means the number of possible combinations is about 1 googol (10 to the 100th power - more possible combinations than there are atoms in the known universe).

But one benefit of the URL being a long list of English words is that you can memorize it using a mnemonic tool if you have to, and you can easily read it out loud to someone.

# How to Securely Share Your Chat Room's URL

So you might be wondering - what's the most secure way to share a URL to my new LeapChat room?

In this case, you should use some sort of self-destructing redirect URL. That way, even if someone discovers the URL in one of your messages after you've already used it, they won't know where the link ultimately lead.

You can use an open source service like [One Time Secret](https://onetimesecret.com) to share your URL.

And how about file sharing? You could just securely share a text file containing the link to your secure chat room using Keybase or Signal if you want to set those up.

But there's an even easier way. Mozilla offers [an anonymous end-to-end encrypted file sharing service for files up to 1 gigabyte](https://send.firefox.com). You can even set the download links to expire after you use them.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Firefox_Send.jpg)

# How To Keep Moles Out of Your Chat Room

Now you have all the tools you need to create a truly private, truly secure group chat with your friends. But how do you identify whether your friends are who they say they are?

Any organization will have a potential "mole" problem.

If an intruder can manage to get inside your group, it doesn't matter how seriously you practice security. They can just do whatever privacy countermeasures you tell them to do and continue to have access.

So before you transition your group to a more secure location, you need to establish that the people in your group are who they say they are.

Assuming people in the group are supposed to know who one another are (and that it's not a meeting of anonymous people), I have a pretty sure-fire way to accomplish this. It's similar to Keybase's approach of confirming your identity using public posts to social media. But my method is even more discreet.

All you need to do is to ask them to update their LinkedIn profile to include a random word, like "pizzicato". Then you can check their LinkedIn profile to confirm that they have control over it.

LinkedIn is a great social network to use for this because almost every professional has one. It's a hassle to create a new account and accumulate real-world connections and endorsements. They don't need to create a post - they can just update their profile long enough for you to verify they are who they say they are, and can then revert their profile change.

So once a member of your current chat has passed your real-world ID check, you can give them a self-destructing URL that leads to your LeapChat room, or exchange Signal or Keybase encryption keys, then chat there.

# How to Delete Your Existing Discord / Slack / Twitter DM Community

The bad news is most of these services will continue to store your data long after you've deleted your account.

Even if you explicitly ask them to delete all of your data, there's just no way to know for sure your data has been deleted. It's impossible to prove your data no longer exists in some backup somewhere.

What is done is done. What is said is said.

But you do have control over what companies are able to store about you in the future.

If you have admin access to your old Discord or a Slack, you can delete it. And even if this doesn't actually delete all the data form their servers, it will prevent new people from being able to join the group and sift through your chat history. It will reduce the likelihood of any of your secrets getting out in the future.

You can also delete your own accounts on the Slacks and Discords that you're a part of. This should remove your old messages.

# Again, here's how to migrate your Slack, Discord, other group chat over to a more secure home - all in one flowchart.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/An_untitled_mindmap.jpg)

# A couple bonus tools if you really, really want to be secure

## Browse with Tor

Tor stands for “The Onion Router” which is a reference to its use of many onion-like layers to mask network activity. It’s free, open source, and reasonably easy to use.

Tor feels like any other browser, and has a similar feature set. It's a fork of Firefox. It's just a bit slower because of all the additional packet redirection. 

But if you really want to browse the web with peace of mind, use Tor and it will be virtually impossible for anyone to track you.

[Download the Tor Browser here](https://www.torproject.org/download/).

Once you've installed Tor, you can visit [check.torproject.org](https://check.torproject.org/) to verify that everything is working right.

## Use a Protonmail Account for Email

![Image](https://www.freecodecamp.org/news/content/images/2020/01/Secure_email__ProtonMail_is_free_encrypted_email_.jpg)

[Protonmail](https://protonmail.com/) is a privacy-focused email tool. You know it's secure because it's Swiss. ?

You will need to give Protonmail a real email address in order to create your account, but this email address will be stored in encrypted form.

You will probably want more than one Protonmail address for each purpose.

Also remember that emails are also stored on the servers of your recipient's mail service. So if you email someone who has a Gmail address, your email is also going to be stored in Google's servers.

## That's it. Stay vigilant, friends.

