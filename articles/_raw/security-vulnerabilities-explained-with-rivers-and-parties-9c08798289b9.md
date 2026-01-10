---
title: Security Vulnerabilities Explained with Rivers and Parties
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-18T18:02:39.000Z'
originalURL: https://freecodecamp.org/news/security-vulnerabilities-explained-with-rivers-and-parties-9c08798289b9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9d26Q5AQW9j1rsCPaqzh-Q.jpeg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Andrea Zanin

  Security vulnerabilities can be boring to learn. But you still need to learn them,
  unless you want some hacker to delete all your production databases. To make it
  a bit more entertaining, I tried to explain 3 major vulnerabilities in ...'
---

By Andrea Zanin

Security vulnerabilities can be boring to learn. But you still need to learn them, unless you want some hacker to delete all your production databases. To make it a bit more entertaining, I tried to explain 3 major vulnerabilities in terms of every day life. So without further delay let’s begin.

### Man-in-the-middle attack

When you open a website you are connecting to a server. You can imagine this connection like a river and the data (for example Tweets in Twitter) are messages in bottles that float down the river.

If Alex (the server) wants to send you a dinner invitation he has to put it in a bottle and send it down the stream. But what if John (the attacker) takes the bottle out of the river and changes the message into an insult, then puts it back in the river? You will have no way of recognizing that the message you received hadn’t been sent by the Alex!

This is called a **Man-in-the-middle attack**.

To solve this you and Alex can decide that you will write your messages reversing the order of the characters. For example, **secret message** becomes **egassem terces**.

John doesn’t know the **method** you used to generate the secret code, so he can’t understand what the message says nor change what’s written on it without you noticing.

This is what the **HTTPS** protocol does, just with a fancier method.

### DoS and DDoS

Another way you can see a server is like your home’s Inbox. You receive mail, read them and reply.

What if John starts to write you a ton of mail? You wouldn’t be able to respond to Alex’s dinner invitation in time, because you would be too busy replying to all the other Spam messages sent by John.

This is called a **Denial-of-service attack**, DoS in short.

A way to mitigate this is reading the sender on top of the mail before opening it. If it’s John then don’t bother opening the mail. This way you don’t need to reply to John and can focus on handling serious stuff, like Alex’s dinner invitation.

This is **IP Blacklisting** in a nutshell, only with digital sender internet protocol addresses.

Unfortunately John convinced a lot of other evil people to send you Spam mails. So now you can’t simply discard John’s mails, because there are lots of people writing you.

This is a **Distributed Denial of Service (DDoS)** and it’s very hard to deal with.

One way to handle this is to receive mail only from Alex. It’s unfortunate that your other friends won’t be able to write you, because you will discard their emails too. But desperate times call for desperate measures. But gradually, you can increase the number of legitimate people you’d like to receive mail from.

This is called **IP Whitelisting** and can be used to mitigate the impact of a DDoS attack, but it’s not a perfect solution.

DDoS attacks are hard to deal with, luckily they are also hard to organize, because you need a lot of people helping you. But with attackers leveraging vulnerable IOT devices, misconfigured servers and DDoS-for-hire services to launch DDoS attacks, it is becoming very easy to launch such attacks.

### Injection

Let’s say that Alex decided that he will organize a party with some friends. He prepared a template invitation:

> Next Saturday I’m throwing a party, wanna come? If possible bring some [blank space left for food item here].  
> Tom

He also decided to take suggestions for the food, so he left a suggestion box in the school’s cafeteria. Then he mindlessly copied one suggestion from the box in the blank space left on each invitation.

These were the suggestions:

* coke
* chips
* pasta
* oranges. I also wanted to tell you that Rick is dumb

You see what’s going on here? A friend of Tom’s will receive this message

> Next Saturday I’m throwing a party, wanna come? If possible bring some oranges. I also wanted to tell you that Rick is dumb.  
> Tom

Tom’s friend will think that the whole message was written by Tom including the part regarding Rick! The guy who left the food suggestion (I think we know his name) just **injected** a message in Alex’s invitation.

To avoid **injection** all together simply validate (in technical lingo **escape**) what you are accepting from a user when it doesn’t come from a trusted source.

### Before you leave

If your name is John I owe you an apology, but stick around, I promise that in the next article you will be the good one.

I hope you enjoyed the article. Don’t forget that you can ? up to 50 times!

