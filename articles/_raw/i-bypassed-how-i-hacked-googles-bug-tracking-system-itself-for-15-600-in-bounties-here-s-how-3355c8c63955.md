---
title: I bypassed “How I hacked Google’s bug tracking system itself for $15,600 in
  bounties.” Here’s how.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-23T18:09:35.000Z'
originalURL: https://freecodecamp.org/news/i-bypassed-how-i-hacked-googles-bug-tracking-system-itself-for-15-600-in-bounties-here-s-how-3355c8c63955
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FnYAmegCjYie3tJD31dW7A.jpeg
tags:
- name: bug bounty
  slug: bug-bounty
- name: Google
  slug: google
- name: General Programming
  slug: programming
- name: Security
  slug: security
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Gopal Singh

  Hello Everyone!

  I was reading some write-ups, and I came across this bug which I liked: “Getting
  a Google employee account.” It was a nice find by Alex Birsan. I started testing
  the issue tracker, and I was trying to see if I could get...'
---

By Gopal Singh

Hello Everyone!

I was reading some write-ups, and I came across this bug which I liked: [“Getting a Google employee account](https://medium.freecodecamp.org/messing-with-the-google-buganizer-system-for-15-600-in-bounties-58f86cc9f9a5).” It was a nice find by [Alex Birsan](https://www.freecodecamp.org/news/i-bypassed-how-i-hacked-googles-bug-tracking-system-itself-for-15-600-in-bounties-here-s-how-3355c8c63955/undefined). I started testing the issue tracker, and I was trying to see if I could get a Google account. Then looking around in issue tracker, I noticed in the browse components there were two public issue trackers. So I clicked on Android Public Tracker.

I could see bugs reported to Android there. To report a Bug in the Android public issue tracker, you can send an email to:

**buganizer-system+**_componentID_**@google.com**

where android’s component id is 190923.

I could see that my issue got listed in the public issue tracker. I got a confirmation email from **buganizersystem+my_email@google.com.** A reply to this email would be directed to:

**buganizer-system+**_componentID**+**issueID_**@google.com**

I responded to that email, and a comment was posted in the conversation. I could add a Google email to see if I could get a confirmation code. To test this I clicked on [Forwarding and POP/IMAP](https://mail.google.com/mail/u/0/#settings/fwdandpop) in Gmail settings and added the Google email to the forwarding email address. I was surprised to see I got a confirmation code in the Android public issue tracker.

There are two parts here to get a Google account **Signup** and **verification**. I could verify a Google account, but I could not signup for an @google.com account, so my report was closed as Won’t Fix. I almost gave up, because after the initial fix I could not use my google.com email. But I decided to give it one last try.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VPKKHkJihwBU5EGmiCO87Q.jpeg)

Then I started visiting every sub-domain of Google to see if I could use a google.com email to signup. This new signup page appeared (see below). Initially, I could not find “Use my current email address instead” to get it to go to [https://partnerissuetracker.corp.google.com/](https://partnerissuetracker.corp.google.com/). Then you would click on Create an account, and you could see there was an option to use your current email address.

![Image](https://cdn-media-1.freecodecamp.org/images/1*FnYAmegCjYie3tJD31dW7A.jpeg)

My heart rate increased after seeing the new signup page. I began to sign up using the **buganizer-system+**_componentID**+**issueID_**@google.com** email and then it asked me to verify by entering the code.

#### Verify your email address

I was waiting for the verification code in the conversation, and then I received the verification code in the email and the conversation in the issue tracker.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2V5EtNmYL9dLuWzzE5Pahg.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*i3SoADa-WPpR624Nr9BPyA.jpeg)

After successfully signing up for the Google Account, I reopened the issue. The impact here was that you can access [https://google.ridecell.com](https://google.ridecell.com) which requires a Google account. Besides this, I tried to upgrade my account to Gmail now as I had a Google account. I added it to my Gmail, and I was able to send an email using from **buganizer-system+**_componentID**+**issueID_**@google.com**

If you try to spoof google.com email, your mail will land in spam. But my email appeared in the inbox, and it was from @google.com so an attacker could pretend that they were a Google employee.

#### **Nice catch!**

![Image](https://cdn-media-1.freecodecamp.org/images/1*OM8Cx-NTdPsFxkGJgMcqxQ.jpeg)

It was 9:50 PM when I was looking for bugs, and finally, the most awaited email arrived: I was getting **$3133.70**. I could not sleep the whole night.

![Image](https://cdn-media-1.freecodecamp.org/images/1*cp_Noolq5VnWPNf3NqgNGg.jpeg)

Check out this video to see more:

Thanks to [Alex Birsan](https://www.freecodecamp.org/news/i-bypassed-how-i-hacked-googles-bug-tracking-system-itself-for-15-600-in-bounties-here-s-how-3355c8c63955/undefined) — this would not have been possible without his write-up. I learned a lot from reading his write-up. Also, thanks to [Avinash Jain](https://www.freecodecamp.org/news/i-bypassed-how-i-hacked-googles-bug-tracking-system-itself-for-15-600-in-bounties-here-s-how-3355c8c63955/undefined) and [Alex Birsan](https://www.freecodecamp.org/news/i-bypassed-how-i-hacked-googles-bug-tracking-system-itself-for-15-600-in-bounties-here-s-how-3355c8c63955/undefined) for taking the time to review the draft.

Thanks for reading!

[Gopal Singh](https://www.freecodecamp.org/news/i-bypassed-how-i-hacked-googles-bug-tracking-system-itself-for-15-600-in-bounties-here-s-how-3355c8c63955/undefined) ([https://twitter.com/gopalsinghcse](https://twitter.com/gopalsinghcse))

