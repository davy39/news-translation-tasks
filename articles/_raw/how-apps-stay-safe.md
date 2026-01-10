---
title: 'How to stay safe on the Internet: it’s proxy servers all the way down'
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2019-09-17T13:15:00.000Z'
originalURL: https://freecodecamp.org/news/how-apps-stay-safe
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/Victoria-drake-image.png
tags:
- name: Application Security
  slug: application-security
- name: servers
  slug: servers
seo_title: null
seo_desc: 'This article is an overview of how proxy servers form the basis of online
  anonymity. We''ll discuss how you can use proxies to help both users and web applications.

  One core aspect of online privacy is the use of a proxy server - though this basic
  bui...'
---

This article is an overview of how proxy servers form the basis of online anonymity. We'll discuss how you can use proxies to help both users and web applications.

One core aspect of online privacy is the use of a proxy server - though this basic building block may not be visible underneath its more recognizable forms.

Proxy servers are a useful thing to know about nowadays, for developers, software product owners, as well as the average dog on the Internet. 

Let’s explore what makes proxy servers an important piece of cybersecurity support.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Internet_dog.jpg)
_“On the Internet, nobody knows you’re a dog.” Comic by Peter Steiner of The New Yorker._

When [Peter Steiner’s comic](https://en.wikipedia.org/wiki/On_the_Internet,_nobody_knows_you%27re_a_dog) was first published in The New Yorker in 1993, it reportedly went largely unnoticed. Only later did the ominous and slightly frightening allusion to online anonymity touch the public consciousness with the icy fingers of the unknown. 

As internet usage became more popular, users became concerned that other people could represent themselves online in any manner they chose, without anyone else knowing who they truly were.

This - to make a gross understatement - is no longer the case. Thanks to [tracking cookies](https://support.mozilla.org/en-US/kb/enable-and-disable-cookies-website-preferences), [browser fingerprinting](https://robertheaton.com/2017/10/17/we-see-you-democratizing-de-anonymization/), [Internet Service Providers (ISPs) selling your browsing logs to advertisers](https://www.privacypolicies.com/blog/isp-tracking-you/), and your own inexplicable inclination to put your name and face on social networks, online anonymity is out like last year’s LaCroix flavours.

Your next-door neighbor may not know how to find you online (well, except for through that location-based secondhand marketplace app you’re using), but you can be certain that at least one large advertising company has a series of zeroes and ones somewhere that represent you, the specific details of your market demographic, and all your online habits. Including your preferred flavour of LaCroix.

There are ways to add _some_ layers of obscurity, like using a corporate firewall that hides your IP, or [using Tor](https://www.torproject.org/). 

The underlying mechanism of both these methods is the same. Like being enshrouded in the layers of an onion, you’re using one or more [proxy servers](https://en.wikipedia.org/wiki/Proxy_server) to shield your slightly sulfuric self from third-party tracking.

#### What’s a proxy server, anyway?

A proxy, in the traditional English definition, is the “authority or power to act for another.” ([Merriam-Webster](https://www.merriam-webster.com/dictionary/proxy)) A proxy server, in the computing context, is a server that acts on behalf of another server, or a user’s machine.

By using a proxy to browse the Internet, for example, a user can defer being personally identifiable. All of the user’s Internet traffic appears to come from the proxy server instead of their machine.

#### Proxy servers are for users

There are a few ways that you, as the client, can use a proxy server to conceal your identity when you go online. It’s important to know that these methods offer differing levels of anonymity, and that no single method will really provide _true_ anonymity. 

If others are actively seeking to find you on the Internet, for whatever reason, you should take further steps to make your activity harder to identify. (Those steps are beyond the scope of this article, but you can get started with the [Electronic Frontier Foundation’s (EFF) Surveillance Self-Defense](https://ssd.eff.org/) resource.) 

For the average dog on the Internet, however, here is a small menu of options ranging from least to most anonymous.

#### Use a proxy in your web browser

Certain web browsers, including Firefox and Safari on Mac, allow you to configure them to send your Internet traffic through a proxy server. 

The proxy server attempts to [anonymize](https://en.wikipedia.org/wiki/Anonymizer) your requests by replacing your originating IP address with the proxy server’s own IP address. This provides you with some anonymity, as the website you’re trying to reach will not see your originating IP address. However, the proxy server that you choose to use will know exactly who originated the request.

This method also doesn’t necessarily encrypt traffic, block cookies, or stop social media and cross-site trackers from following you around; on the upside, it’s the method least likely to prevent websites that use cookies from functioning properly.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/0_07snWvA_wsI_deAm.png)

Public proxy servers are out there. Deciding whether you should use any one of them is on par with deciding whether you should eat a piece of candy handed to you by a smiling stranger.

If your academic institution or company provides a proxy server address, it is (hopefully) a private server with some security in place.

My preferred method, if you have a little time and a few monthly dollars to invest in security, is to set up your own virtual instance with a company such as [Amazon Web Services](https://aws.amazon.com/ec2/) or [Digital Ocean](https://www.digitalocean.com/products/droplets/) and use this as your proxy server.

To use a proxy through your browser, you can [edit your Connection Settings in Firefox](https://support.mozilla.org/en-US/kb/connection-settings-firefox), or [set up a proxy server using Safari on Mac](https://support.apple.com/guide/safari/set-up-a-proxy-server-ibrw1053/mac).

In regards to choosing a browser, I would happily recommend [Firefox](https://www.mozilla.org/en-US/firefox/new/) to any Internet user who wants to beef up the security of their browsing experience right out of the box. 

Mozilla has been a champion of privacy-first since I’ve heard of them, and recently made some well-received changes to [Enhanced Tracking Protection in Firefox Browser](https://blog.mozilla.org/blog/2019/06/04/firefox-now-available-with-enhanced-tracking-protection-by-default/) that blocks social media trackers, cross-site tracking cookies, fingerprinters, and cryptominers by default.

#### Use a VPN on your device

In order to take advantage of a proxy server for all your Internet usage instead of just through one browser, you can use a Virtual Private Network (VPN). 

A VPN is a service, usually paid, that sends your Internet traffic through their servers, thus acting as a proxy. A VPN can be used on your laptop as well as phone and tablet devices, and since it encompasses all your Internet traffic, it doesn’t require much extra effort to use other than ensuring your device is connected. 

Using a VPN is an effective way to keep nosy ISPs from snooping on your requests.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/1_B8XYVrDTlI8KXcm27dFmUQ.png)

To use a paid, third-party VPN service, you'd usually sign up on their website and download their app. It’s important to keep in mind that whichever provider you choose, you’re entrusting them with your data. 

VPN providers anonymize your activity from the Internet, but can themselves see all your requests. Providers vary in terms of their privacy policies and the data they choose to log, so a little research may be necessary to determine which, if any, you are comfortable trusting.

You can also roll your own VPN service by using a virtual instance and [OpenVPN](https://openvpn.net/). OpenVPN is an open source VPN protocol, and can be used with a few virtual instance providers, such as [Amazon VPC](https://openvpn.net/amazon-cloud/), [Microsoft Azure](https://openvpn.net/microsoft-azure/), [Google Cloud](https://openvpn.net/google-cloud-vpn/), and [Digital Ocean Droplets](https://openvpn.net/digital-ocean-vpn/). 

I previously wrote a tutorial on [setting up your own personal VPN service with AWS](https://victoria.dev/verbose/how-to-set-up-openvpn-on-aws-ec2-and-fix-dns-leaks-on-ubuntu-18.04-lts/) using an EC2 instance. I’ve been running this solution personally for about a month, and it’s cost me almost $4 USD in total, which is a price I’m quite comfortable paying for some peace of mind.

#### Use Tor

Tor takes the anonymity offered by a proxy server and compounds it by forwarding your requests through a [relay network](https://en.wikipedia.org/wiki/Relay_network) of other servers, each called a “node.” 

Your traffic passes through three nodes on its way to a destination: the _guard_, _middle_, and _exit_ nodes. At each step, the request is encrypted and anonymized such that the current node only knows where to send it, and nothing more about what the request contains.

This separation of knowledge means that, of the options discussed, Tor provides the most complete version of anonymity. (For a more complete explanation, see [Robert Heaton’s article on how Tor works](https://robertheaton.com/2019/04/06/how-does-tor-work/), which is so excellently done that I wish I’d written it myself.)

![Image](https://www.freecodecamp.org/news/content/images/2019/09/1_S-lzVbWxv3Y_iskGZ3aCwQ.png)

That said, this level of anonymity comes with its own cost. Not monetary, as [Tor Browser](https://www.torproject.org/download/) is free to download and use. It is, however, slower than using a VPN or simple proxy server through a browser, due to the circuitous route your requests take.

#### Proxy servers are for servers too

Now you're familiar with proxy servers in the context of protecting users as they surf the web. However, proxies aren’t just for clients. Websites and Internet-connected applications can use [reverse proxy servers](https://en.wikipedia.org/wiki/Reverse_proxy) for obfuscation too. The “reverse” part just means that the proxy is acting on behalf of the server, instead of the client.

Why would a web server care about anonymity? Generally, they don’t. At least not in the same way some users do. 

Web servers can benefit from using a proxy for a few different reasons. For example, they typically offer faster service to users by [caching](https://en.wikipedia.org/wiki/Web_cache) or [compressing](https://en.wikipedia.org/wiki/HTTP_compression) content to optimize delivery. 

From a cybersecurity perspective, however, a reverse proxy can improve an application’s security posture by obfuscating the underlying infrastructure.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/1_9SL4Lh-A5dFsQSaCHT2Ekw.png)

Basically, by placing another web server (the “proxy”) in front of the web server that directly accesses all the files and assets, you make it more difficult for an attacker to pinpoint your “real” web server and mess with your stuff. 

Like when you want to see the store manager and the clerk you’re talking to says, “I speak for the manager,” and you’re not really sure there even _is_ a manager, anyway, but you successfully exchange the hot pink My Little Pony they sold you for a _fuchsia_ one, thankyouverymuch, so now you’re no longer concerned with who the manager is and whether or not they really exist, and if you passed them on the street you would not be able to stop them and call them out for passing off hot pink as fuchsia, and the manager is just fine with that.

Some common web servers can also act as reverse proxies, often with just a minimal and straightforward configuration change. While the best choice for your particular architecture is unknown to me, I will offer a couple common examples here.

#### Using NGINX as a reverse proxy

NGINX uses the `proxy_pass` directive in its [configuration file](https://docs.nginx.com/nginx/admin-guide/basic-functionality/managing-configuration-files/) (`nginx.conf` by default) to turn itself into a reverse proxy server. The set up requires the following lines to be placed in the configuration file:

```
location /requested/path/ {proxy_pass http://www.example.com/target/path/;}
```

This specifies that all requests for the path `/requested/path/` are forwarded to `http://www.example.com/target/path/`. The target can be a domain name or an IP address, the latter with or without a port.

The full [guide to using NGINX as a reverse proxy](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/) is part of the NGINX documentation.

#### Using Apache httpd as a reverse proxy

Apache httpd similarly requires some straightforward configuration to act as a reverse proxy server. In the [configuration file](https://httpd.apache.org/docs/current/configuring.html), usually `httpd.conf`, set the following directives:

```
ProxyPass "/requested/path/" "http://www.example.com/target/path/"ProxyPassReverse "/requested/path/" "http://www.example.com/target/path/"
```

The `ProxyPass` directive ensures that all requests for the path `/requested/path/` are forwarded to `http://www.example.com/target/path/`. The `ProxyPassReverse` directive ensures that the headers sent by the web server are modified to point to the reverse proxy server instead.

The full [reverse proxy guide for Apache HTTP server](https://httpd.apache.org/docs/2.4/howto/reverse_proxy.html) is available in their documentation.

#### Proxy servers _most of_ the way down

I concede that my title is a little facetious, as cybersecurity best practices aren’t really some eternal infinite-regression mystery (though they may sometimes seem to be). 

Regardless, I hope this post has helped in your understanding of what proxy servers are, how they contribute to online anonymity for both clients and servers, and that they are an integral building block of cybersecurity practices.

If you’d like to learn more about personal best practices for online security, I highly recommend exploring the articles and resources provided by [EFF](https://www.eff.org/). For a guide to securing web sites and applications, the [OWASP Cheat Sheet Series](https://github.com/OWASP/CheatSheetSeries) is a fantastic resource.

