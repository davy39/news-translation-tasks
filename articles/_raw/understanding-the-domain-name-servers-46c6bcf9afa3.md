---
title: An introduction to the Domain Name System
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-23T09:14:51.000Z'
originalURL: https://freecodecamp.org/news/understanding-the-domain-name-servers-46c6bcf9afa3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DlTgMe5CZ5BfICp6i42f-g.jpeg
tags:
- name: computer network
  slug: computer-network
- name: dns
  slug: dns
- name: internet
  slug: internet
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Sumedh Nimkarde

  You all might have heard about or know about the Domain Name System (DNS) if you
  understand how the internet works or how computer networks work. If you aren’t familiar
  with DNS, I would recommend that you go and check out my previ...'
---

By Sumedh Nimkarde

You all might have heard about or know about the Domain Name System (DNS) if you understand how the internet works or how computer networks work. If you aren’t familiar with DNS, I would recommend that you go and check out my previous blog post which is focused on computer networks [here](https://medium.freecodecamp.org/computer-networks-and-how-to-actually-understand-them-c1401908172d).

Hostnames alone cannot tell us where the particular machine/hardware that we are trying to communicate with is located in the world. Hence, all communication is done with IP addresses.

Domain Name Servers are the devices that map the hostname to the IP addresses of the machine/hardware on which your services are running.

In this post, I will be explaining in detail the types of DNS queries, types of DNS servers, and types of DNS records.

### DNS Resolver

DNS Resolvers are the computers used by Internet Service Providers (ISPs) to perform lookups in their database for the particular hostname requested by the user. They then redirect that user to the mapped IP address. They play a vital role in DNS Resolution.

DNS Resolvers also cache the data. So for example, my website`example.com` is currently hosted on a machine with the IP address `35.195.226.230` . So, the caches of the DNS Resolvers all over the world have mapped the following:

`example.com` -&g`t; 35.195.226.`230

Consider, in the future, if I want to host my website on any another server across the world with an IP of, say, `35.192.247.235`. The DNS caches of all the DNS Resolvers across the world will still have the old IP address for some time. This may lead to unavailability through conventional means of the website until the DNS propagation happens completely.

The record in the DNS Resolver cache remains there for some time, which is called time to live (TTL for short).

This is the time a record is cached in the DNS Resolver. This can be set in the registrar’s dashboard from where you have purchased the domain.

Note: from now on, I will refer to the DNS Resolver as Resolver only in this blog post.

### Types of DNS servers

#### **Root DNS server**

The Root DNS servers are the ones who have the addresses of all the TLD domain servers. A request first encounters the Root DNS servers while on its journey to obtain the IP address from the hostname.

There are 13 root domain name servers across the world as of 2016. This does not mean that there are only 13 machines handling the load of the requests coming from all over the world — there are multiple servers at ground level handling the load.

Different organizations manage the Root DNS servers:

![Image](https://cdn-media-1.freecodecamp.org/images/B3BTLHU-knwsZx4JFN91eiiBt-vlJvaepjeS)
_Credits: https://iana.org_

#### **TLD domain server**

These are the ones classified according to the Top-Level Domain. They are usually the next ones which the iterative query hits after the Root DNS server. They store the TLD specific records for the hostname.

Let’s say if we are requesting an IP address of `medium.com` , then the TLD domain servers for “.com” TLD are queried. The TLD domain servers return the address of the Authoritative DNS servers to the Resolver.

![Image](https://cdn-media-1.freecodecamp.org/images/dY2lnrWhjllbEIQl9Wy7TwUxtwYLi7AsGX-R)
_Fig. TLD Name servers pointing to the Authoritative Name servers_

Now, the question arises: how does the TLD name server know the address of the Authoritative Name server? The answer is simple: when you purchase any domain with the registrars like Godaddy or Namecheap, the registrars also communicate the domains to the TLD name server. So it is able to contact the Authoritative Name servers.

Nowadays, some of the registrars provide the ability to use third party Authoritative Name servers. As shown in the above figure, you can set up the Authoritative Nameservers in the registrar’s dashboard.

#### **Authoritative DNS server**

These are queried iteratively in the end by the Resolver. They store the actual records for type A, NS, CNAME, TXT, etc.

Thus, they return the IP address of the hostname if available. If it is not available even in the Authoritative DNS server, then they throw an error with the particular message and the process of searching IP addresses across the Nameserver ends.

### Types of DNS queries

There are three types of DNS queries:

**Recursive**: Recursive queries are made by users to the Resolver. It is actually the first query made while doing any DNS lookup.

The Resolvers can be your ISP or your network admin, but usually, it is the ISP in almost all cases.

**Non-recursive:** in non-recursive queries, the Resolver knows the answer and responds immediately without making any further queries to any other name servers. This happens because the local DNS server has the IP address stored in its local cache or it just queries the Authoritative name servers directly. They happen to definitely hold the record and this eventually avoids the recursive queries.

**Iterative**: Iterative queries happen when the Resolver cannot return the results since they may not have cached it. So, it makes a request to the Root DNS server. And the Root DNS servers know where to find the particular TLD domain server.

So, for example, if we are trying to obtain the IP address for say `medium.com` , then the Root domain server will have the address of the `.com` TLD server stored in it and will then send it back to the Resolver. The Resolver then asks the TLD server for the IP address. The TLD domain server may not know it, but it knows the address of the Authoritative DNS server for `medium.com` .

Okay, enough of the theory. Let’s understand it by a flow diagram:

![Image](https://cdn-media-1.freecodecamp.org/images/5U6XICe32XPfFiNDXob5e6tM1EzcIJE7tV7i)
_Fig. DNS Resolution_

Let’s break down the above diagram in steps:

1. The user makes a request to the Resolver with the hostname for which it wants the IP address. This is a recursive query.
2. The Resolver does a lookup in its cache to see if it is present in it.
3. If it is, it returns it back to the user.
4. If it does not have it cached, it makes an iterative request to the Root DNS servers that are present globally. As of 2016, there are 13 Root DNS servers named from A — M. Now, the Root DNS server looks up for the TLD of the requested domain. For example, if the hostname is `medium.com` , then the TLD becomes “.com” and the Root DNS server has the entry for “.com” domain servers and it returns the results back to the Resolver. The Resolver must have the addresses of all the Root domain name servers. If it doesn’t, the DNS lookup may fail in the first place.
5. Now, the Resolver again makes an iterative request to the TLD domain server asking for the IP address of the domain. The TLD domain server then returns back the address of the Authoritative server for the requested domain.
6. As of now, I believe, you may understand what are Authoritative DNS servers. They contain the actual records where the hostname is mapped to the IP address and hence the IP address is returned back to the Resolver (which in turn returns it back to the user).
7. If no matching record is found in the Authoritative Name servers, then an error with a message saying “DNS_PROBE_FINISHED_NXDOMAIN” is thrown indicating there is no record for the requested hostname.
8. In all the Nameservers the request passes through, the results for the requested hostname are cached so that when any other user requests the same domain, the record will already be present in the DNS cache.
9. All in all, it takes at the max four queries to perform the DNS lookup. But, it hardly takes a few milliseconds to perform the lookup.

#### **The concept of DNS Propagation**

Consider, you have your website hosted with some provider like Digital Ocean on any machine with IP “x”, and you want to shift the website hosting to any other machine with different IP address say “y”. You will have to change the IP address in the Authoritative records so that traffic navigates to the new IP address.

Even if you update the records in your registrar’s/ name server’s dashboard, it takes some time to reflect in all the Resolvers’ caches in the world. DNS propagation can take 24–72 hours, but usually it happens sooner than that since most ISPs keep the TTL low.

And that’s it!

Thanks for reading the article. If you have any questions, please feel free to ask them in the comments below and share this post with whomever you want.

See you in the next one. Have a great time. Thank you.

You can check out my other article on Computer Networks which explains them in detail:

[**What computer networks are and how to actually understand them**](https://medium.freecodecamp.org/computer-networks-and-how-to-actually-understand-them-c1401908172d)  
[_Whether you are new to the world of development, or have been building things for a long time — or even if you’re a…_medium.freecodecamp.org](https://medium.freecodecamp.org/computer-networks-and-how-to-actually-understand-them-c1401908172d)

If you like my work, you can buy me a coffee at:

[**Buy Sumedh Nimkarde a Coffee - BuyMeACoffee.com**](http://buymeacoffee.com/lunaticmonk)  
[_Hello, I am Sumedh and my work is to build, break and rebuild things._buymeacoffee.com](http://buymeacoffee.com/lunaticmonk)

Feel free to reach out to me on [Twitter](https://twitter.com/lunatic_monk).

