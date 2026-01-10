---
title: What you need to know about DNS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-12T21:07:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-dns-anyway
coverImage: https://www.freecodecamp.org/news/content/images/2019/06/nasa-53884-unsplash.jpg
tags:
- name: cybersecurity
  slug: cybersecurity
- name: internet
  slug: internet
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Megan Kaczanowski

  What is DNS lookup?

  Domain Name System Lookup, or DNS for short, is what happens in the time between
  someone typing a URL into the search bar and the page loading. Technically speaking,
  it is a process that translates URLs (like ...'
---

By Megan Kaczanowski

### What is DNS lookup?

Domain Name System Lookup, or DNS for short, is what happens in the time between someone typing a URL into the search bar and the page loading. Technically speaking, it is a process that translates URLs (like [www.google.com)](http://www.google.com%29) into IP addresses. 

An IP address is similar to your house address. Just as you use addresses to send mail, computers use IP addresses to send data to a specific place. Since IP addresses are hard to remember (they are long strings of numbers), computers use DNS to translate between IP addresses and URLs (which are much easier to remember). All internet-connected devices have an IP address.

### How does DNS work?

Given the size of the internet, computers cannot store all IP addresses in their memory. Instead, typing [www.google.com](http://www.google.com) into a browser tells the computer to look up the IP address for the website.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screen-Shot-2019-06-13-at-5.00.46-PM.png)

First, the computer checks its local memory, called its cache. This is where the computer stores its most recently visited sites’ IP addresses, so it can load them faster without having to look them up. However, since only a few recently visited sites are here, chances are, the computer does not find the IP address.

**Step 1  (steps correspond with the diagram numbers above):** Next, the computer will ask the ISP’s local recursive nameserver. An ISP is an internet service provider — like Time Warner Cable, Spectrum, Verizon, etc. A nameserver sounds complicated, but is just server software that is designed to answer DNS requests (such as “what is the IP address for www.google.com?”). 

Any nameserver can answer this question, by either responding with the IP address (if it knows), or responding that it does not know and telling the requesting server to ask a different server. A recursive nameserver is different because if it does not know the answer to the question. It will do the work of finding the answer, instead of merely re-directing the query. Not all nameservers are recursive.

**Step 2:** The recursive nameserver will check its cache first. If the IP address is not there, it will ask a root nameserver (root nameservers do not know IP addresses, but they can read requests and tell the recursive nameserver where to go next). All recursive nameservers come with 13 root nameservers’ IP addresses pre-configured. The recursive nameserver picks one and asks it the same question (“what is the IP address for www.google.com?”).

**Step 3:** The root nameserver reads the top-level domain (the end of the request), in this case .com, (www.google.com) and will tell the recursive nameserver to ask the Global Top Level Domain Servers (GTLD). GTLDs are essentially reference lists for each type of domain — .com, .net., .edu, etc. While they don’t know the IP addresses for websites, they do know which nameservers will have that information.

**Step 4:** The recursive nameserver asks the GTLD nameserver for www.google.com’s IP address.

**Step 5:** The GTLD nameserver will read the next part of your request, reading from right to left (in this case the ‘google’ of [www.google.com)](http://www.google.com%29) and will send back a message with the authoritative nameserver to contact. An authoritative nameserver is a nameserver that is responsible for the domain (and is the primary source of information).

**Step 6:** The recursive nameserver will ask the authoritative nameserver the same question (“what is the IP address for www.google.com?”). Technically, the server is asking for the Address Record (A), which is how servers refer to the IP address.

**Step 7:** This server has the answer! It will pass the IP address back to the recursive nameserver, flagged to let the recursive nameserver know the answer is authoritative. The recursive nameserver files the IP address in its cache in case someone tries to access the same website soon. Each item in the cache is tagged with a “time to live” that tells the server how long to hold the information before deleting it.

**Step 8:** The recursive nameserver tells your computer what the IP address is (it isn’t tagged as authoritative this time, because it is not the primary source of information. It is just passing the information along.

**Step 9:** Your computer sends a request for [www.google.com](http://www.google.com) to the IP address it just received.

**Step 10:** The web server at this address returns the google homepage and the page loads.

This entire process takes only a few milliseconds to complete and happens trillions of times every day.

### How does DNS impact end users?

As DNS is integral to the internet functioning, it is a prominent target for hackers.  The root problem with DNS is the same as most security problems we experience with today's technology. The internet, and much of the technology we use today was designed for a small group of researchers and over time expanded into a system which the entire world uses. DNS (and HTTP, and most of the protocols we use) were not designed with security in mind. Now, we've had to add on fixes for various security issues. Unfortunately, security bolted-on at the end is not as effective as security baked into the development. 

One problem this poses for DNS is that there isn't any verification of the authenticity of the name server when a response is received. Thus a hacker can send malicious responses to a computer’s DNS query and trick the computer into thinking that it is the real response from the DNS nameserver. In other words, when the computer asks, “what is the IP address for www.chase.com?” the hacker will respond (before the DNS server can) with the IP address for the hacker’s malicious site . Then when the site loads, it looks just like the chase.com website, but is actually controlled by the hacker. 

This is very similar to phishing — except that users aren’t being tricked into clicking on bad links, but rather the websites they’re trying to visit are being routed to bad sites through DNS lookup (much more dangerous, as it is much harder to prevent these type of attacks). This then requires the user to be wary, to notice that the site is spoofing the real site (perhaps the link doesn't look quite right, or there are misspellings or poor logo copies). However, this can be very difficult and relies upon users to be relatively technically savy. 

In 2016, a DNS attack knocked out significant parts of the internet for most of the east coast of the United States for almost a full day.In that case, the outage was caused by a DDoS attack. A DDoS attack is a distributed-denial-of-service attack, in which thousands of machines across the internet attack a system at the same time. Generally, these are machines that have been infected with malware without their owner’s knowledge, and one hacker, or group of hackers, is controlling all the machines. These machines are called a ‘botnet’ when used together. 

The botnet sends DNS requests to the victim server and the amount of requests sent overwhelms the system, rendering the server unable to handle the legitimate traffic it receives. Thus, while hackers are attacking DNS servers and a computer tries to request IP addresses, the server is unable to respond. So the computer cannot access the sites that server controls (or is authoritative for) until the attack is stopped.

This attack can be mitigated against by over-provisioning servers in order to handle excess demand or having a DNS firewall.

A broader way to approach solving many of the problems presented by DNS is DNSSEC. DNSSEC strengthens authentication with digital signatures based on public key cryptography. Essentially the owner of the requested data digitally signs it, in order to ensure that the above situation can't happen. This provides data origin authentication (the data actually came from where the resolver thinks it came from) and data integrity protection (the data hasn't been modified in transit).

Unfortunately, in order to fix DNS, DNSSEC requires wide deployment. It needs to be specifically enabled by network operators on their recursive resolvers, and by domain name owners on authoritative servers. This hasn't yet happened, but hopefully will as more people become aware of the issues DNS presents and advocate for changes.






