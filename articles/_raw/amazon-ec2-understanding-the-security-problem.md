---
title: Amazon EC2 – Understanding and Addressing the Security Problem
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-05-18T19:07:42.000Z'
originalURL: https://freecodecamp.org/news/amazon-ec2-understanding-the-security-problem
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/pexels-pixabay-277574.jpg
tags:
- name: AWS
  slug: aws
- name: cybersecurity
  slug: cybersecurity
- name: information security
  slug: information-security
seo_title: null
seo_desc: "Hi there. Great to have you here. But I'm afraid I'm going to have to start\
  \ off with some bad news. \nBefore you can really improve the security of your Amazon\
  \ EC2 instances, you'll need to get a handle on all the stuff that can go wrong.\
  \ And I'll giv..."
---

Hi there. Great to have you here. But I'm afraid I'm going to have to start off with some bad news. 

Before you can really improve the security of your Amazon EC2 instances, you'll need to get a handle on all the stuff that can go wrong. And I'll give you a bit of a "hall of shame" rundown in just a minute. 

## What's the Problem?

But first, by way of introduction, I want to tell you a really scary story. So scary, that you should perhaps prepare by turning on all the lights in your room and grabbing a soft blanket for comfort.

Here goes. Based on my own past experiences, I just conducted a brief experiment. I launched an EC2 instance running Ubuntu into one of my AWS accounts. The instance wasn't running anything more than whatever Ubuntu gave me by default and it wasn't associated with any DNS addresses. 

Its only connection with the outside world was through the public IP address AWS assigned it. In fact, the only difference between this instance and one that you or I might normally run is that I opened up its security group to permit all incoming traffic. 

Since Ubuntu, by default, doesn't run an active firewall, there would therefore be nothing standing between the instance and the big bad internet.

This article comes from my [Securing Your AWS EC2 Instances course](https://www.udemy.com/course/securing-amazon-ec2-instances/?referralCode=E3ACB9DC5E3B77853E63). If you'd like, you can follow the video version of this section here:

%[https://www.youtube.com/watch?v=femqe6OIJGk&list=PLSiZCpRYoTZ5dys7oy4ReI-ltW0jnGTMO&]

So what happened? Well, the `auth.log` entries on the host were astounding. According to those logs, the system came up for the first time at around 14:56. Here's a little of what I saw just 35 minutes later:

![Image](https://www.freecodecamp.org/news/content/images/2023/03/ec2_security1-f004258.png)

Someone was trying to log in to my system via SSH using the user name `root`. Now, of course, by default, root login is disabled - and you should leave it that way. But that didn't stop this individual from trying. 

Note how they didn't just use the standard SSH port 22, but played around with alternative port numbers (including `51912` as well). That suggests that this attempt was part of an automated script that tests various combinations of usernames, passwords, and ports:

```
Aug 10 15:31:17 ip-172-30-1-186 sshd[2777]: error: maximum authentication attempts exceeded for root from 20.210.53.189 port 51912 ssh2 [preauth]

```

But they weren't done. Over the next 75 seconds, 30 more login attempts came from this same IP address. They pointed to different ports in the 50,000 range, and used different usernames like, admin, oracle, test, test1, test2, ftpuser, and pi. 

The fact that they tried `pi` tells me that they didn't realize that this was a cloud instance but that, for all they knew, it could have been a Raspberry Pi running in someone's home lab.

I don't know about you, but I find this really frightening. Sure, which admin would purposely open up a security group to all incoming traffic? But the real point is that there are so many scripts out there constantly scanning for live IP addresses and then trying to brute force system logins, that any random IP address can expect hits within minutes. 

And, again, this isn't the first time I've seen this in action, nor is SSH the only public-facing service that attracts such attacks. At the very least, we should take this as a warning to tighten up our SSH configurations - which is something I will discuss later.

But here's the thing. It _is_ possible to achieve perfect security - it really is - but that would involve completely locking your servers down and blocking all access from the outside world. What's the point of running servers like that? The goal is to find the best possible balance between application functionality and infrastructure security. 

Establishing that balance might include incorporating all the general IT security basics like system hardening and monitoring, alongside the intelligent use of key AWS security features like IAM roles, security groups, appropriate VPC architectures and, where appropriate, the use of VPNs.

So just what's out there waiting to dig its claws into your AWS operations? Well there are hackers' tools for getting into your system, exploits for taking over and misusing your resources, and methodologies for bringing down your services by force. Let's look at these one at a time.

## Access Acquisition

As you might have noticed from the `maximum authentication attempts exceeded` content of those log entries I showed you earlier, the hacker tried entering multiple passwords for each login name. 

That's known as a brute force attack, where hackers rotate through a dictionary of common passwords, hoping that one will turn out to be correct. 

The reason my system cut those attempts off completely is because the official EC2 Linux images have a default SSH configuration setting - `MaxAuthTries` - set to six. Even if you did permit password logins for SSH - and even if you did irresponsibly use a weak password - the odds against a hacker getting it right within six tries are pretty slim.

If you'd like, you can follow the video version of the second part of the article here:

%[https://www.youtube.com/watch?v=Ajwoe9sSjuo&list=PLSiZCpRYoTZ5dys7oy4ReI-ltW0jnGTMO&]

Of course, if a hacker can get hold of _real, active_ credentials, then they won't need to guess. That's why you should be aware of phishing attacks where hackers use social manipulation to get victims to unknowingly reveal their login information. 

They can similarly take advantage of communications that take place using compromised devices or that are sent over unencrypted connections to sniff your credentials as you use them.

In _cloud_ terms, just imagine how much fun someone could have once they get hold of your AWS account credentials. That would allow them to quickly run up hundreds of thousands of dollars worth of bills on your credit card, by deploying nearly endless AWS resources in service of their own criminal needs. Besides having to cover those bills, you might also get blamed for any crimes committed with those resources.

## Exploits

Once hackers have gained access to your system, things can only get worse. Whether they do something nasty right away or hang around for months planning something particularly nefarious, if you don't catch them at it, eventually they'll install their malware. 

That might take the shape of keyboard trackers that record every character you and your colleagues enter in a shell session. It'll only be a matter of time before those trackers capture credentials that'll let them elevate their own permissions.

The malware could also take the form of cryptocurrency mining operations that make heavy - and expensive - use of your system resources so the hackers can profit. Or - and this is the most frightening - they might decide to encrypt key data on your drives and demand large payments before they'll let you decrypt and regain access. 

This, of course, is known as ransomware, and it's currently the biggest problem facing enterprise-level systems. It costs governments and companies billions of dollars each year.

## Service Disruption

Even if they don't get _into_ your system, the bad guys can still do a lot of damage from the outside. If, for instance, they detect misconfigurations on your servers - like unnecessarily open network listening ports, poorly written database endpoints, or outdated software like FTP or telnet, they can cause you plenty of problems.

And, for those criminals with access to networks of hijacked zombie servers, they could overrun your network capacity with distributed denial of service attacks - preventing your legitimate users from accessing your services. 

Fortunately, AWS provides some serious protection from DDoS out of the box, so that's not likely to be a big concern for you as an admin.

Speaking of AWS engineering, now's probably a good time to discuss their [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/). The way the company phrases it, AWS is responsible for the security _of the cloud_ while their customers - that would be you and me - are responsible for the security of whatever you put _in the cloud_.

Practically, that means you don't need to worry about terrible things happening to the physical servers and storage devices used by your EC2 instances. AWS will protect their warehouses and networking hardware from unauthenticated intrusion and harm. They'll also take responsibility for the software powering any of their managed services - like the API and dashboards you use to configure account activity.

But you're responsible for everything else. That includes the data your instances might generate and the operating systems themselves. So you're on the hook for keeping your operating system and application software patched, and for making appropriate backups of all the data and configuration files you generate.

You're also responsible for making the right AWS-level configuration choices, like getting your security group and network settings right. Depending on the industry and national jurisdiction within which you operate, you might also be expected to meet one or more regulatory compliance standards. 

AWS provides documentation laying out which standards each service meets. If you open the web page shown below, you could expand the Payment Card Industry - PCI - section, for instance, and then search for EC2. You'll see that EC2 infrastructure is, indeed, PCI-compliant;

![Image](https://www.freecodecamp.org/news/content/images/2023/03/services_in_scope.png)

We've seen how vulnerable your EC2 instances are when they're left without adequate protection. But we've also seen some industry best-practices for keeping them secure. You know what your next step is.

_This article comes from my [Securing Your AWS EC2 Instances course](https://www.udemy.com/course/securing-amazon-ec2-instances/?referralCode=E3ACB9DC5E3B77853E63). And there's much more technology goodness available at [bootstrap-it.com](https://bootstrap-it.com/)_

