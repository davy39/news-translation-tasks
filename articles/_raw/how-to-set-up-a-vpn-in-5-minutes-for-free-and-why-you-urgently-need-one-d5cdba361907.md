---
title: How to set up a VPN in 10 minutes for free (and why you urgently need one)
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2017-03-27T15:21:07.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-a-vpn-in-5-minutes-for-free-and-why-you-urgently-need-one-d5cdba361907
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qg1G0C-hpkG-hO4rd5eVdg.jpeg
tags:
- name: Life lessons
  slug: life-lessons
- name: politics
  slug: politics
- name: Security
  slug: security
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: '“A computer lets you make more mistakes faster than any other invention
  with the possible exceptions of handguns and Tequila.” — Mitch Ratcliffe


  Soon every mistake you’ve ever made online will not only be available to your internet
  service provider ...'
---

> “A computer lets you make more mistakes faster than any other invention with the possible exceptions of handguns and Tequila.” — Mitch Ratcliffe

Soon every mistake you’ve ever made online will not only be available to your internet service provider (ISP) — it will be available to any corporation or foreign government who wants to see those mistakes.

Thanks to a decision by Congress, ISPs can sell your entire web browsing history to literally anyone without your permission. The only rules that prevented this are all being repealed, and won’t be reinstated any time soon (it would take an act of congress).

ISPs can also sell [any information they want](https://www.washingtonpost.com/news/the-switch/wp/2017/03/28/republicans-are-poised-to-roll-back-landmark-fcc-privacy-rules-heres-what-you-need-to-know/) from your online activity and mobile app usage — financial information, medical information, your children’s information, your social security number — even the contents of your emails.

They can even sell your geolocation information. That’s right, ISPs can take your exact physical location from minute to minute and sell it to a third party.

You might be wondering: who benefits from repealing these protections? Other than those [four monopoly ISPs](https://medium.freecodecamp.com/inside-the-invisible-war-for-the-open-internet-dd31a29a3f08) that control America’s “last mile” of internet cables and cell towers?

No one. No one else benefits in any way. Our privacy — and our nation’s security — have been diminished, just so a few mega-corporations can make a little extra cash.

In other words, these politicians — [who have received millions of dollars in campaign contributions](http://www.theverge.com/2017/3/29/15100620/congress-fcc-isp-web-browsing-privacy-fire-sale) from the ISPs for decades — have sold us out.

### How did this happen?

The Congressional Review Act (CRA) was passed in 1996 to allow Congress to overrule regulations created by government agencies.

Prior to 2017, congress had only successfully used the CRA once. But since the new administration took over in January, it’s been successfully used 3 times — for things like overturning pesky environmental regulations.

Senator Jeff Flake — a Republican representing Arizona — led the effort to overturn the FCC’s privacy rules. He was already [the most unpopular senator in the US](https://www.theatlantic.com/politics/archive/2013/04/jeff-flake-most-unpopular-senator-america/315763/). Now he may become the most unpopular senator in US history.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zqZq3wF3E2GY1xBYSXLBUw.jpeg)
_Senator Flake_

Instead of just blaming Flake, though, let’s remember that every single senator who voted in favor of overturning these privacy rules was a Republican. Every single Democrat and Independent senator voted against this CRA resolution. The final vote was 50–48, with two Republicans abstaining.

You would think that the Senate would heavily discuss such the consequences of such an historic decision. Actually, [they only spent 10 minutes debating it](https://www.congress.gov/congressional-record/2017/03/23/senate-section/article/S1942-4).

> “Relying on the government to protect your privacy is like asking a peeping tom to install your window blinds.” — John Perry Barlow

![Image](https://cdn-media-1.freecodecamp.org/images/1*Rw4q1vi2p-xDw9Bgo0kfwg.jpeg)
_VPN company [Private Internet Access](https://www.privateinternetaccess.com/" rel="noopener" target="_blank" title=") paid $600,000 to run this full-page ad in Sunday’s New York Times — even though they would make a ton of money if these rules were repealed. That’s how bad things have gotten with this CRA — even the VPN companies are campaigning against it._

[The CRA resolution](https://www.congress.gov/bill/115th-congress/senate-joint-resolution/34/text) also passed in the House of Representatives, where 231 Republicans voted in favor of removing privacy protections against 189 Democrats who voted against it. (Again, not a single non-Republican voted to remove these privacy protections.)

All that’s left is for the Republican president to sign the resolution, which he has said he plans to do.

### So what kind of messed-up things can ISPs now legally do with our data?

According to the [Electronic Frontier Foundation](https://www.eff.org/deeplinks/2017/03/five-creepy-things-your-isp-could-do-if-congress-repeals-fccs-privacy-protections), there are at least five creepy things the FCC regulations would have made illegal. But thanks to the Senate, ISPs can now continue doing these things as much as they want, and it will probably be years before we can do anything to stop them.

1. Sell your browsing history to basically any corporation or government that wants to buy it
2. Hijack your searches and share them with third parties
3. Monitor all your traffic by injecting their own malware-filled ads into the websites you visit
4. Stuff undetectable, un-deletable tracking cookies into all of your non-encrypted traffic
5. Pre-install software on phones that will monitor all traffic — even HTTPS traffic — before it gets encrypted. AT&T, Sprint, and T-Mobile have already done this with some Android phones.

### So how do we have any hope of protecting our privacy now?

According to a [study by the Pew Research Center](http://www.pewresearch.org/fact-tank/2016/09/21/the-state-of-privacy-in-america/), 91% of adults agree or strongly agree that “consumers have lost control of how personal information is collected and used by companies.”

But we shouldn’t despair. But as the same British Prime Minister who cautioned us to “hope for the best and prepare for the worst” also said:

> “Despair is the conclusion of fools.” — Benjamin Disraeli in 1883

Well we are not fools. We’re going to take the actions necessary to secure our family’s privacy against the acts of reckless monopolies and their political puppets.

And we’re going to do this using the most effective tools for securing online communication: encryption and VPNs.

### Step 1: enable HTTPS Everywhere

As I mentioned, ISPs can work around HTTPS if they are able to factory-install spyware on your phone’s operating system. As long as you can avoid buying those models of phones, HTTPS will give you a huge amount of additional protection.

HTTPS works by encrypting traffic between destination websites and your device by using the secure TLS protocol.

The problem is that, as of 2017, only about 10% of websites have enabled HTTPS, and even many of those websites haven’t properly configured their systems to disallow insecure non-HTTPS traffic (even though it’s free and easy to do using [LetsEncrypt](https://letsencrypt.org/)).

This is where the EFF’s HTTPS Everywhere extension comes in handy. It will make these websites default to HTTPS, and will alert you if you try and access a site that isn’t HTTPS. It’s free and you can [install it here](https://www.eff.org/https-everywhere).

One thing we know for sure — thanks to the recent [WikiLeaks release of the CIA’s hacking arsenal](https://medium.freecodecamp.com/the-cia-just-lost-control-of-its-hacking-arsenal-heres-what-you-need-to-know-ea69fc1ce38c) — is that [encryption still works](http://bigstory.ap.org/article/cf84bf54c2954de8baaa5fb6931a84d0/what-cia-wikileaks-dump-tells-us-encryption-works). As long as you’re using secure forms of encryption that haven’t yet been cracked — and as far as we know, HTTPS’s TLS encryption hasn’t been — your data will remain private.

> “The average busy professional in this country wakes up in the morning, goes to work, comes home, takes care of personal and family obligations, and then goes to sleep, unaware that he or she likely committed several federal crimes that day.” — Harvey Silverglate

By the way, if you haven’t already, I strongly recommend you read my article on [how to encrypt your entire life in less than an hour](https://medium.freecodecamp.com/tor-signal-and-beyond-a-law-abiding-citizens-guide-to-privacy-1a593f2104c3#.rouhl2kbf).

But even with HTTPS enabled, ISPs will still know — thanks to their role in actually connecting you to websites themselves — what websites you’re visiting, even if they don’t know what you’re doing there.

And just knowing where you’re going — the “metadata” of your web activity — gives ISPs a lot of information they can sell.

For example, someone visiting Cars.com may be in the market for a new car, and someone visiting BabyCenter.com may be pregnant.

That’s where using a VPN comes in.

### How VPNs can protect you

VPN stands for Virtual Private Network.

* **Virtual** because you’re not creating a new physical connection with your destination — your data is just traveling through existing wires between you and your destination.
* **Private** because it encrypts your activity before sending it, then decrypts it at the destination.

People have traditionally used VPNs as a way to get around websites that are blocked in their country (for example, Medium is blocked in Malaysia) or to watch movies that aren’t available in certain countries. But VPNs are extremely useful for privacy, too.

There are several types of VPN options, with varying degrees of convenience and security.

Experts estimate that [as many as 90% of VPNs are “hopelessly insecure”](https://www.theregister.co.uk/2016/02/26/ssl_vpns_survey/) and this changes from time to time. So even if you use the tools I recommend here, I recommend you take the time to [do your homework](https://thatoneprivacysite.net/simple-vpn-comparison-chart/).

### Browser-based VPNs

Most VPNs are services that cost money. But the first VPN option I’m going to tell you about is convenient and completely free.

Opera is a popular web browser that comes with some excellent privacy features, like a free built-in VPN and a free ad blocker (and as you may know, ads can spy on you).

If you just want a secure way to browse the web without ISPs being able to easily snoop on you and sell your data, Opera is a great start. Let’s install and configure it real quick. This takes less than 5 minutes.

Before you get started, note that this will only anonymize the things you do within the Opera browser. Also, I’m obligated to point out that even though Opera’s parent company is European, it was recently [purchased](https://www.engadget.com/2016/07/18/opera-browser-sold-to-a-chinese-consortium-for-600-million/) by a consortium of Chinese tech companies, and there is a non-zero risk that it could be compromised by the Chinese government.

Having said that, here’s how to browse securely with Opera:

Step #1: [Download the Opera browser](http://www.opera.com/download)

Step #2: Turn on its ad blocker

![Image](https://cdn-media-1.freecodecamp.org/images/1*Svu1s-f68d70nvAFVy80-Q.png)

Step #3: Turn on its VPN

![Image](https://cdn-media-1.freecodecamp.org/images/1*QIZSUyCzs6vuZjhezL6qRQ.png)

Step #4: Install HTTPS Everywhere

When you’re done, Opera should look like this:

![Image](https://cdn-media-1.freecodecamp.org/images/1*45iHcNJX5Zm1RM0Ivw7jUg.png)

Presto — you can now browse the web with reasonable confidence that your ISPs — or really anyone else —don’t know who you are or what you’re doing.

![Image](https://cdn-media-1.freecodecamp.org/images/1*xCkk-sZNoP2TbJUZ_Mj8cw.png)

You can even set your VPN to a different country. Here, I’ve set mine to Singapore so websites will think I’m in Singapore. To test this out, I visited [ipleak.net](https://ipleak.net/) and they did indeed think I was in Singapore.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Tro90X97Lt6VwG8wkzsUdQ.png)

Since the internet is complex, and data passes through hundreds of providers through [a system of peering and trading traffic](https://medium.freecodecamp.com/inside-the-invisible-war-for-the-open-internet-dd31a29a3f08), US-based ISPs shouldn’t be able to monitor my traffic when it emerges from Singapore.

If you want to take things next level, you can try Tor, which is extremely private, and extremely hard to de-anonymize (though it can be done, [as depicted in the TV show Mr. Robot](https://medium.freecodecamp.com/all-i-really-need-to-know-about-infosec-i-learned-from-mr-robot-7902cca6d729#.nhwv27j9v) — though it would require incredible resources).

Tor’s a bit more work to set up and use, and is slower than using a VPN. If you want to learn more, I have a getting-started guide for Tor [here](https://medium.freecodecamp.com/tor-signal-and-beyond-a-law-abiding-citizens-guide-to-privacy-1a593f2104c3#.rouhl2kbf).

### VPN Services

The most common way people get VPNs is through a monthly service. There are a ton of these. Ultimately, you must trust the company running the VPN, because there’s no way to know what they’re doing with your data.

As I said, some VPNs are improperly configured, and may leak personally identifying data.

Before you buy a VPN, read up on how it compares to others [here](https://thatoneprivacysite.net/vpn-comparison-chart/). Once you buy a VPN, the best way to double check that it’s working properly is to visit [ipleak.net](https://ipleak.net/) while using the VPN.

Even though most users of VPNs are companies with remote employees, the NSA will still [put you on a list if you purchased a VPN](https://www.wired.com/2014/07/nsa-targets-users-of-privacy-services/). So I recommend using something anonymous to do so, like a pre-loaded Visa card. (By the way, [Bitcoin is not anonymous](https://bitcoin.org/en/you-need-to-know).)

There are dozens of VPN services, and there’s no clear “winner.” I use [Private Internet Access](https://www.privateinternetaccess.com/) which costs about $40 per year and runs on my family’s computers and phones.

I also asked people on Twitter which VPNs they were using and got a variety of answers:

### Routers with built-in VPNs

You can purchase a VPN-enabled router. Note that these aren’t specifically designed to protect you from snooping by your ISP. Instead, they’re designed so that companies’ satellite offices can share the same network as their headquarter offices. I haven’t used one before, so I can’t testify to their efficacy.

If you happen to have a second residence in a county outside the US, you can just tunnel through that home’s network. Otherwise, you’ll need to configure your router to work with one of the VPN services I mentioned earlier.

Some routers are designed to work with VPNs at higher speeds than others. If you want to use a VPN at the router level, and your internet connection is less than 100 mps, [this router](http://amzn.to/2nPUsMU) will probably suffice. Otherwise, you’ll need to pay a bit more for a router [like this one](http://amzn.to/2n1JLTB).

If you don’t trust the router companies, you can modify a router using [Tomato USB](https://en.wikipedia.org/wiki/Tomato_(firmware)). It’s an alternative open source Linux-based router firmware that’s compatible with some off-the-shelf routers.

### Privacy is hard. But it’s worth it.

Privacy is a fundamental human right, and has been [declared so by the United Nations](http://www.un.org/en/universal-declaration-human-rights/).

Still, many people believe we live in a “post-privacy” era. For example, Mark Zuckerberg claims privacy isn’t that important any more. But look at his actions. He paid $30 million to buy the 4 houses adjacent to his Palo Alto home [so he could have more privacy](http://www.businessinsider.com/mark-zuckerberg-buys-4-homes-for-privacy-2013-10).

Other people are just too jaded and shell-shocked by all the data breaches around us to believe that privacy is still worth the fight.

But most people who say they don’t care about their own privacy anymore just haven’t really given it much thought.

> “Arguing that you don’t care about the right to privacy because you have nothing to hide is no different than saying you don’t care about free speech because you have nothing to say.” — Edward Snowden

Last week’s US Senate vote is just the latest in a series of events that show how we can’t trust governments to act in the interest of consumers when it comes to their privacy.

We need stronger privacy protections enshrined in the law.

In the meantime, we’ll just have to look out for ourselves, and educate other people to do the same.

I encourage you to read computer security expert Bruce Schneier’s book “[Data and Goliath: The Hidden Battles to Collect Your Data and Control Your World](http://amzn.to/2mjheuO).” I learned a ton from it, and am listening to it a second time.

[**Data and Goliath: The Hidden Battles to Capture Your Data and Control Your World**](http://amzn.to/2mjheuO)  
[_Edit description_amzn.to](http://amzn.to/2mjheuO)

Thanks for reading, and for taking privacy seriously.

If you liked this, please share it on social media.

