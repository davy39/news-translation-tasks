---
title: Why a domain’s root can’t be a CNAME — and other tidbits about the DNS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-13T23:00:07.000Z'
originalURL: https://freecodecamp.org/news/why-cant-a-domain-s-root-be-a-cname-8cbab38e5f5c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YNkO-BfTsVJYxslNrNn8LA.jpeg
tags:
- name: dns
  slug: dns
- name: internet
  slug: internet
- name: programing
  slug: programing
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Dominic Fraser

  This post will use the above question to explore DNS, dig, A records, CNAME records,
  and ALIAS/ANAME records from a beginner’s perspective. So let’s get started.

  First, some definitions


  Domain Name System (DNS): the overall system ...'
---

By Dominic Fraser

This post will use the above question to explore `DNS`, `dig`, `A` records, `CNAME` records, and `ALIAS/ANAME` records from a beginner’s perspective. So let’s get started.

### First, some definitions

* **Domain Name System** (DNS): the overall system for converting a human memorable domain name (example.com) to an IP address (93.184.216.34). The IP address is of a server, commonly a web server, where the files needed to display a webpage are stored.
* **DNS Server** (also known as a name server or nameserver): Uses DNS software to store information about domain addresses. There are several levels — those belonging to each ISP, Root (13 total worldwide), Top Level Domain (TLD, e.g. ‘.com’), and Domain level DNS Servers.
* **Domain name**: the domain (example) combined with the TLD (.com). The term ‘domain’ is often used synonymously with the domain name, [though they are different](https://www.domainsherpa.com/anatomy-of-a-domain-name-and-url/). When you buy a ‘domain’ from a a registrar or reseller, you buy the rights to a specific domain name (example.com), and any subdomains you want to create (my-site.example.com, mail.example.com, etc).

### High level query flow

The high-level flow of what happens when you type “example.com” into your browser can be simplified to remove the hops to the ISP, Root, and TLD DNS Servers as below:

![Image](https://cdn-media-1.freecodecamp.org/images/-Yu9MR65z19xx2TDl-6phT7soy3g3KNgjArX)
_Simplified DNS request flow, more can be seen in a [more detailed flow](http://www.uxworld.com/?p=384" rel="noopener" target="_blank" title=")_

A domain typically has two or more name servers, containing records relating to the domain name (example.com).

Many types of records can be stored, most of which can have multiple entries per type:

* `A`: Address records that map the domain name to an IP address
* `CNAME`: Canonical Name Record. Used to alias one domain name (or subdomain name) to another. We’ll look at this in more detail later.
* `MX`: Mail eXchange records that tell email delivery agents where they should deliver your email
* `TXT`: flexible Text records, for storing strings for a variety of uses
* `SOA`: singular Start of Authority record kept at the top level of the domain. Contains specific required information about the domain, for example its primary name server
* `NS`: The name servers associated with the domain

When your device sends a query that reaches a name server, the server looks in the domain’s record node for an `A` record, and the associated stored IP address (example.com: 93.184.216.34). This is then returned to the device, to be used to send a request to the correct web server to retrieve the requested webpage or resource.

### Using ‘dig’

`dig` (**domain information groper**) is a command-line tool for querying DNS servers. This command is generally used for troubleshooting, or as now to understand more about the setup of a system.

`$ dig example.com` results in a long response printed to the terminal, the [default output detailed here](https://www.madboa.com/geek/dig/#understanding-the-default-output), of which we are interested in the `ANSWER SECTION`.

```
;; ANSWER SECTION:
example.com.       72703      IN     A       93.184.216.34
```

And there we go, we can see that `example.com` returns an `A` record of `93.184.216.34`. Sometimes domains will have more than one `A` record, if more than one web server can provide the information needed.

There’s more! If we try out some other examples, we can soon see that another common record appears: `CNAME`.

`$ dig www.skyscanner.net`:

```
;; ANSWER SECTION:
www.skyscanner.net. 169 IN CNAME www.skyscanner.net.edgekey.net.
www.skyscanner.net.edgekey.net. 5639 IN CNAME e11316.a.akamaiedge.net.
e11316.a.akamaiedge.net. 20 IN A 23.217.6.192
```

```
www.skyscanner.net.edgekey.net. 5639 IN CNAME e11316.a.akamaiedge.net.
```

```
e11316.a.akamaiedge.net. 20 IN A 23.217.6.192
```

Using the `+short` flag allows us to clearly see the path formed:

`$ dig [www.skyscanner.net](http://www.skyscanner.net) +short`

```
www.skyscanner.net.edgekey.net.
e11316.a.akamaiedge.net.
23.217.6.192
```

### CNAME

A `CNAME` record allows a domain name to be used as an alias for another canonical (true) domain.

When the DNS server returns a `CNAME` record, it will not return that to the client. Rather it will again look up the returned domain name, and in turn return the `A` record’s IP address. This chain can continue many `CNAME` levels deep, but then suffers minor performance hits from multiple lookups before caching takes place.

A simple example of this could be if you have a server where you keep all your photos. You may normally access it through `photos.example.com`. However, you might also want it to allow access via `photographs.example.com`. One way to make this possible is to add a `CNAME` record that points `photographs` to `photos`. This means that when someone visits `photographs.example.com` they would be given the same content as `photos.example.com`.

Using the query `$ dig photographs.example.com` we would see:

```
photographs.example.com    IN   CNAME photos.example.com
photos.example.com         IN   A     xx.xxx.x.xxx
```

It’s important to note that the `CNAME` is that piece to the right hand side. The left hand side is the alias name, or label.

Another common use is for the `www` subdomain. Having purchased `example.com` you likely also want users who type in `www.example.com` to see the same content.

It is worth noting here that `example.com` can be called the apex, root, or naked domain name.

One option would be to set up another `A` record, pointing to the same IP address as for `example.com`. This is completely valid, and is what the real `example.com` does, but it does not scale well. What happens if you need to update the IP address that `example.com` points to? You would also need to update it for the `www` subdomain, and any others you may use.

If a `CNAME` record was used to alias `www.example.com` to point to `example.com` then only the root domain would have to be updated, as all other nodes point to it.

### CNAME limitations

At the time when the DNS standards were written, some rules were set out to govern their use. [RFC 1912](https://tools.ietf.org/html/rfc1912) and [RFC 2181](https://tools.ietf.org/html/rfc2181) set out that:

* `SOA` and `NS` records are mandatory to be present at the root domain
* `CNAME` records can only exist as single records and can not be combined with any other resource record ( DNSSEC `SIG`, `NXT`, and `KEY RR` records excepted)

This excludes a `CNAME` being used on the root domain, as the two rules would contradict each other.

What’s important here is that this is a contractual limitation, not a technical one. It is possible to use a `CNAME` at the root, but it can result in unexpected errors, as it is breaking the expected contract of behavior.

An example of this is [told by Cloudflare](https://blog.cloudflare.com/introducing-cname-flattening-rfc-compliant-cnames-at-a-domains-root/), describing problems they encountered with Microsoft Exchange mail servers after having used a `CNAME` on their root domain:

> Domains generally designate the servers that handle their email through what’s known as a MX Record. The problem was that Exchange servers … could pick up the CNAME at the root record and then not properly respect the CNAME set at the MX record. You can’t really blame Exchange. **They were operating under the assumptions laid out by the DNS specification.**

Here you see the downside that can appear in several server softwares or libraries. Because a standard is in place for a `CNAME` to be the **only** record at a node, **no other records are looked for.** All other records will be silently ignored, without warning or error messages. Even if an `MX` record was set to receive email, the `MX` will be ignored as if it doesn’t exist because the `CNAME` is evaluated first. The same is true if there were an `A` record: the `CNAME` would take precedence and the `A` record would not be read.

### The modern internet

So why is this a problem? Why would you ever want to use a `CNAME` for your root domain anyway? Surely that is the end of the path when looking for the IP address of the web server hosting your content?

In the modern internet landscape, that is no longer the case. The world is very different from when the DNS standards were written.

You may choose to use a Platform as a Service (PaaS) provider like [Heroku](https://www.heroku.com/) and store content on their web servers. You control the content, but not the infrastructure, and the PaaS provider does the heavy lifting of the network maintenance. They typically provide you with a URL (`my-app.herokuapp.com`) that is a subdomain of their root domain, and you can view the IP addresses for the web server(s) your content is on. But these are entirely under the PaaS provider’s control, and will change without warning.

The scale and frequency of backend changes made by the PaaS provider can make it hard to maintain your root domain `A` record pointing at a single IP address. Ideally you would wish to do this:

```
example.com      IN   CNAME    my-app.herokuapp.com.www.example.com  IN   CNAME    my-app.herokuapp.com.example.com      IN   CNAME    my-app.herokuapp.com.
www.example.com  IN   CNAME    my-app.herokuapp.com.
```

to allow Heroku (or your chosen host provider) to manage updating the `A` record that the `CNAME` points to without any changes made on your side. However, as we now know, this breaks the DNS specification, so is a very bad idea.

It is possible to simply implement a [301/302](https://www.namecheap.com/support/knowledgebase/article.aspx/9604/2237/types-of-domain-redirects--301-302-url-redirects-url-frame-and-cname) redirect from `example.com` to `www.example.com.` However, that instruction takes place either on the web server (so still having the problem of needing to use a fixed `A` record in DNS to point to that web server), or a custom DNS provider redirect (that [suffers complications with HTTPS](https://support.dnsimple.com/articles/url-record/)).

This also has the side effect of changing the domain that you see in the URL bar, which you may not want. This method is intended for when your website has permanently moved, or when you’re trying to [preserve SEO rankings](https://support.google.com/webmasters/answer/93633?hl=en), rather than solving our problem of pointing to a complex changing backend in a scaleable way.

### The solution

Several DNS providers have now developed custom solutions to work around this problem, including:

* `ALIAS` at DNSimple
* `ANAME` at DNS Made Easy
* `ANAME` at easyDNS
* `CNAME` (virtual) at CloudFlare

These are all virtual record types that provide `CNAME` like behaviour, with none of the downsides. The exact implementation can differ, but at a high level when the DNS server sees one of these virtual record types, it acts as a DNS resolver. It follows the chain created by the alias until it resolves at an `A` record (or records) and returns these `A` records to the DNS server. This ‘flattens’ the `CNAME` chain into the `A` record(s) returned, and is indistinguishable to the sent query. The query sees only a pure `A` record, which doesn’t break the DNS specification, and doesn’t have any of the disadvantages of a `CNAME`.

These virtual records can sit alongside other records at the root without any fear of unintended behaviours. Depending on the provider’s method of DNS resolution when following the `CNAME` chain, they may also have performance benefits from caching previous lookups.

For a DNSimple setup, we would then configure as below. This solution has all the advantages of domain name aliasing, and none of the risks of using it at root level.

```
example.com      IN   ALIAS    my-app.herokuapp.com.www.example.com  IN   CNAME    my-app.herokuapp.com.
```

Thanks for reading! ?

_As always, open to any corrections or additional points._

### Resources

* [What is a DNS Server](http://www.itpro.co.uk/domain-name-system-dns/30232/what-is-a-dns-server)
* [Set Up a DNS Name Server](https://www.wired.com/2010/02/Set_Up_a_DNS_Name_Server/)
* [DNSimple support pages](https://support.dnsimple.com/categories/dns/) and [ALIAS blog](https://blog.dnsimple.com/2014/01/why-alias-record/)
* [Cloudflare support](https://support.cloudflare.com/hc/en-us/articles/200169056-CNAME-Flattening-RFC-compliant-support-for-CNAME-at-the-root) and [CNAME blog](https://blog.cloudflare.com/introducing-cname-flattening-rfc-compliant-cnames-at-a-domains-root/)
* `[dig](https://www.madboa.com/geek/dig/)` [HowTo](https://www.madboa.com/geek/dig/)
* [Several](https://stackoverflow.com/questions/656009/how-to-overcome-root-domain-cname-restrictions/22659895#22659895) [great](https://stackoverflow.com/questions/16022324/how-to-setup-dns-for-an-apex-domain-no-www-pointing-to-a-heroku-app) [Stack Overflow](https://stackoverflow.com/questions/655235/is-root-domain-cname-to-other-domain-allowed-by-dns-rfc) or [StackExchange](https://serverfault.com/questions/170194/why-cant-a-domains-root-be-a-cname?noredirect=1&lq=1) [posts](https://serverfault.com/questions/613829/why-cant-a-cname-record-be-used-at-the-apex-aka-root-of-a-domain/613830#613830)
* [Well written](https://en.wikipedia.org/wiki/CNAME_record) Wikipedia entries
* [Netlify blog](https://www.netlify.com/blog/2017/02/28/to-www-or-not-www/) ‘To www or not www’

