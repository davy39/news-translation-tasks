---
title: 'Penetration testing: choosing the right (Linux) tool stack to fix your broken
  IT security'
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2019-07-29T13:00:00.000Z'
originalURL: https://freecodecamp.org/news/penetration-testing-choosing-the-right-linux-tool-stack-to-fix-your-broken-it-security
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/security.jpeg
tags:
- name: Linux
  slug: linux
- name: penetration testing
  slug: penetration-testing
- name: Security
  slug: security
seo_title: null
seo_desc: 'Got IT infrastructure? Do you know how secure it is? The answer will probably
  hurt, but this is the kind of bad news you’re better off getting sooner rather than
  later.

  The only reasonably sure way to find out what’s going on with your servers is to
  ...'
---

Got IT infrastructure? Do you know how secure it is? The answer will probably hurt, but this is the kind of bad news you’re better off getting sooner rather than later.

The only reasonably sure way to find out what’s going on with your servers is to apply a solid round of penetration testing. Your ultimate goal is to uncover any dangerous vulnerabilities so you can lock them down.

By “dangerous vulnerability” I mean obvious things like unprotected open ports and unpatched software. But I also mean the existence of freely available intelligence about your organization that’s probably just floating around the internet, waiting to be collected and turned against you.

Pen testing is made up of three very different parts, each with its own unique tools and protocols.

* **Passive information gathering**, where testers scour the public internet looking for subtle hints or carelessly revealed private data that can be used against the organization.
* **Active information gathering**, where the organization’s networks and servers are scanned for potential vulnerabilities.
* **Identifying exploits** that could possibly be run against the organization’s infrastructure.

Let’s look at those one at a time.

## Passive Information Gathering (OSINT)

Say your company has around 50 employees and a handful of outside contractors, each of whom is most likely active on both professional and personal social networks. And say you’ve got the usual range of corporate and product websites and social media accounts (like LinkedIn).

Now pause for a moment and try to imagine that you’re a hacker who’s searching for exploitable information about your company which he can use to launch an attack. Assuming he’ll stick exclusively to the public internet and not break any laws, how much do you think he’ll find?

Not too much? After all, no one is stupid enough to post passwords and account information to the internet, right?

Perhaps. But you won’t believe how easy it can be to use what **is** there to figure out all the passwords and administration information that hackers will need to get what they’re after. Don’t believe me? Do some passive information gathering yourself.

Among the fantastic/frightening information gathering tools available to help you (which also include Maltego and Shodan) there’s a great Linux-based open source package named Recon-ng — about which I created a [video course on Pluralsight](http://pluralsight.pxf.io/c/1191769/424552/7490?subId1=solving&u=https%3A%2F%2Fapp.pluralsight.com%2Fprofile%2Fauthor%2Fdavid-clinton).

You start by providing Recon-ng with some information about your company and choosing the particular scans that interest you. All the hard work will then be done by tools they call _modules_. Each of the 90+ available modules is a script that reads data from the Recon-ng database and launches a scanning operation against some remote data resource.

Based on your choices, Recon-ng will intelligently comb through vast volumes of DNS, social media, and search engine results, plus information-rich position postings for new developers and hints to internal email addresses relating to your target. When it’s done, the software will prepare a report that’s guaranteed to scare the daylights out of you.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-57.png)
_A text-based report based on a few Recon-ng scans_

With this information, all a hacker would have to do is sift through the data and set the launch date for your attack. With this information, all **you** will have to do is tighten up your defences and speak with your team about being a **lot** more careful when communicating online.

That OSINT acronym I used above? It stands for Open Source Intelligence. Stuff anyone can get.

## Active information gathering (vulnerability assessment)

Besides all the things you thoughtlessly leave lying around across the internet, there’s probably a lot more that a hacker can learn about your infrastructure from the infrastructure itself. If your servers are on a network, it’s because, to some degree, you want them exposed to network users. But that might also expose things you’d rather keep quiet, including the fact that you might be running software that’s buggy and open for exploits.

The good news is that government and industry players — like the US government’s NIST and their [National Vulnerability Database](https://nvd.nist.gov/) — have been actively tracking software vulnerabilities for decades now and they make their information freely available. The bad news is that their databases contain hundreds of thousands of those vulnerabilities and it makes for really dull reading.

You’d like to be able to quickly and regularly scan your network and the devices attached to it to make sure there’s nothing that needs patching, but it’s just not humanly possible to do it manually. So forget humans. You’re going to need software.

Vulnerability scanners are software tools that automatically scan your network and servers for unpatched software, open ports, misconfigured services, and potential exploit vectors (like SQL injection or cross-site scripting). Generally, the software will handle the vulnerability data and search for any matches with what you’ve got running. It’s your job to define the target, set the scan types you want run, read the reports that come out the other end, and — most important of all — fix whatever’s broken.

Commercial scanning packages with free tiers include Nessus, Nexpose, and Burp Suite. OpenVAS is a mature, fully open source tool that can handle just about anything you throw at it. And, most conveniently, it just so happens that my Pluralsight collection also includes a [video guide to using OpenVAS](http://pluralsight.pxf.io/c/1191769/424552/7490?subId1=solving&u=https%3A%2F%2Fapp.pluralsight.com%2Fprofile%2Fauthor%2Fdavid-clinton).

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-58.png)
_The results page of an OpenVAS scan — using their Greenbone browser interface_

An outstanding platform for running all kinds of scans and testing is the Kali Linux distribution. Kali, which itself is highly secure by default, comes with dozens of networking and security software packages pre-configured. OpenVAS, while easily installed to Kali, was left out of the default profile due to its size.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/image-59.png)
_Some pen-testing-friendly software packages available in Kali Linux right out of the box_

It’s common to run Kali within a virtual environment like [VirtualBox](https://hackernoon.com/virtualbox-are-you-getting-your-moneys-worth-4d7f98f3d7d2) rather than having it take up a whole physical machine. That way you can safely isolate your testing from your regular compute activities…not to mention save yourself significant time and money.

## Exploit (penetration) testing

Here (**_after_** obtaining explicit authorization from the organization’s management) is where your pen testers try to actually penetrate your defences to see how far in they can get. Testers will make use of tools like the Metasploit Framework (often also run from Kali Linux), which executes live exploits against target infrastructure. My bad luck: I don’t have a course on Metasploit, but [other Pluralsight authors](http://pluralsight.pxf.io/c/1191769/424552/7490?u=pluralsight.com) sure do.

The immediate goal is to leverage any of the network or operating system exploits discovered during the earlier stages of the scanning process. But the ultimate idea, of course, is to shut down the security flaws your pen tester uncovers. All the testing in the world won’t do you an ounce of good if you don’t use it to improve.

Besides the purely technical hacking tools you’ll use, the exploitation phase of pen testing can also incorporate some good old social engineering. That’s where (when authorized) you can use emails, phone calls, and personal contact to try to fool employees into giving up sensitive information.

It’s a lot of work and requires a great deal of training and preparation to do it well. But if you’re responsible for your company’s IT resources, you can’t leave pen testing for later.

So what’s your next step? If you’re a do-it-yourself type then by all means, carefully work through some online resources or courseware and dive right in. Otherwise, find a professional you can trust and see what they recommend.

Good luck!

_Don’t think I’m just some kind of one-dimensional geek. Besides my_ [_Pluralsight courses_](http://pluralsight.pxf.io/c/1191769/424552/7490?subId1=solving&u=https%3A%2F%2Fapp.pluralsight.com%2Fprofile%2Fauthor%2Fdavid-clinton)_, I also write_ [_books courses on Linux and AWS_](https://bootstrap-it.com/) _and even a hybrid course called_ [_Linux in Motion_](https://www.manning.com/livevideo/linux-in-motion?a_aid=bootstrap-it&a_bid=0c56986f&chan=motion1) _that’s made up of more than two hours of videos and some 40% of the content of my_ [_Linux in Action_](https://www.manning.com/books/linux-in-action?a_aid=bootstrap-it&a_bid=4ca15fc9) _book. Ok. So I suppose I am some kind of one-dimensional geek._

