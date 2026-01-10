---
title: What is ANAME? ANAME Record DNS Tutorial
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-05-02T18:02:19.000Z'
originalURL: https://freecodecamp.org/news/what-is-aname-aname-record-dns-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/alias-1.png
tags:
- name: dns
  slug: dns
- name: domain names
  slug: domain-names
seo_title: null
seo_desc: 'If you’ve ever had to make a domain name work with a website, you’ve probably
  seen ANAME as some record – just like the popular Canonical name record type or
  simply CNAME.

  CNAME and ANAME are both solutions for pointing a hostname to your website. Fo...'
---

If you’ve ever had to make a domain name work with a website, you’ve probably seen ANAME as some record – just like the popular Canonical name record type or simply CNAME.

CNAME and ANAME are both solutions for pointing a hostname to your website. For example, `yourapp.netlify.com` to `yourwebsite.com`.

You’ve probably been using CNAME to make domain names point to websites. But instead, you can use an ANAME which has some added advantages because it gives you more flexibility.

In this article, you will learn what ANAME is, the advantages it has over CNAME, and when to use it.

## What is ANAME?
ANAME, also called ALIAS, is a domain record type that can be used in place of a CNAME record. It's available from domain name companies such as Namecheap, GoDaddy, Hostinger, Google Domain, and more.

ANAME was born out of the combination of CNAME and another record type called A. So, ANAME is a CNAME and A record in one package.

ANAME is not a read DNS record but a way of simulating it. And that’s why it is called Alias name, or ANAME for short.

When you purchase a domain name and log in to its management panel, you will always see an option to use ANAME. 

N.B.: Some domain name providers call it ALIAS instead of ANAME

Below is the Namecheap panel for managing domains and they call it ALIAS.
![alias](https://www.freecodecamp.org/news/content/images/2022/04/alias.png)

## How Does ANAME Work?

Just like CNAME, ANAME maps one domain name to another. So, an ANAME is configured to point to another domain. 

When the domain name an ANAME points to is queried by the client browser, it responds with an IP address. A CNAME, on the other hand, cannot point to an IP address, but an ANAME can. This is one of the advantages ANAME has over CNAME.

In addition, another advantage ANAME has over CNAME is that it can coexist with other records on that domain name. So if you want to have subdomains, you should use ANAME instead of CNAME.

## Final Thoughts

This article explained what ANAME is and compared it with CNAME so you can know the advantages it has over CNAME.

You might also be wondering which to use between ANAME and CNAME, or when you should use one over the other.

This is the logic: 
- if you know you cannot have other records on a domain name, use CNAME. This is because it cannot coexist with other data on the record for a domain name. 
- If you will have other records like subdomain on that domain name, then use ANAME. And if you don’t know whether you'll still have a subdomain or not, use ANAME.

Thank you for reading.


