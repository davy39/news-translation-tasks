---
title: An Introduction to the Akamai Content Delivery Network
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-09T16:46:06.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-the-akamai-content-delivery-network-806aa16d8781
coverImage: https://cdn-media-1.freecodecamp.org/images/1*e-5nwPzNiZtoAIKQOI7VJA.png
tags:
- name: 'content delivery network '
  slug: content-delivery-network
- name: performance
  slug: performance
- name: Security
  slug: security
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Dominic Fraser

  Akamai is one of the world’s leading Content Delivery Network (CDN) providers. Through
  the Akamai Intelligent Platform many products are offered to aid performance, availability,
  security, and insight generation.

  Other CDNs include ...'
---

By Dominic Fraser

Akamai is one of the world’s leading Content Delivery Network (CDN) providers. Through the [Akamai Intelligent Platform](https://www.akamai.com/uk/en/solutions/intelligent-platform/) many products are offered to aid performance, availability, security, and insight generation.

Other CDNs include Cloudflare, Fastly, MaxCDN, Incapsula, and Rackspace.

Here we will look at what a CDN is, then some specifics around Akamai’s implementation, including:

* The Akamai Intelligent Platform and Edge Servers
* The Akamai Interface and Property Manager
* Routing Performance
* Caching

#### What is a CDN?

A user request for content on the public Internet may appear simple, connecting to the server holding the content (the ‘content origin’) and returning this to the user, but it is in fact very complex.

![Image](https://cdn-media-1.freecodecamp.org/images/jDQimdgZxgp-yZlV5hA6yO34Of9rEGZdMIRz)
_Hidden complexity of connecting to the content origin_

The connection may need to go through many Internet Service Providers (ISPs), peering points, and data centres, across competing networks, and suffer from no consistently available routes.

Many different device types and bandwidths may be used, from different global locations, with different content types requested.

This can lead to fluctuating speed and availability, security challenges, and little visibility of what is happening between the user and the content origin.

A CDN places more control in the hands of the content provider, and helps improve the end user experience.

It does this by acting as a parallel high-performance network, maintaining its own network of highly-distributed servers. By being dispersed over many physical and network locations, but optimized as one network, more control and reliability exists for user requests.

As a business grows, scaling to meet higher demands on the content origin also has challenges. We will also look at how CDN tools can be used to reduce load on the origin, helping not just improve performance, but also reduce cost by reducing how high the origin must be scaled.

#### Akamai Intelligent Platform

Akamai maintains a global network of more than 240,000 ‘edge servers’. These are positioned at the ‘edge’ of the Internet, as close to end users as possible. To achieve this many edge servers are even located directly in ISPs, or in mobile data towers, to even greater reduce the latency between connecting to a user’s ISP before moving into the Akamai network.

![Image](https://cdn-media-1.freecodecamp.org/images/sKkZcR-fGy3yMTUTN8BO3uSawcmz7q6rzjK4)
_Akamai network of Edge Servers_

When a user makes a request, Akamai dynamically maps this to the closest available edge server. The edge server applies the business rules that the content provider has specified, before using the best available route between all other edge servers within the Akamai network to fetch content from the origin. Business rules are replicated on each edge server.

Any content available and configured to be cached is then cached on the edge server for future requests connecting to that node. We will look at this in more detail later on.

A site is added to Akamai by adding a [CNAME](https://medium.freecodecamp.org/why-cant-a-domain-s-root-be-a-cname-8cbab38e5f5c) record in DNS that points from the hostname, say ‘community.akamai.com’, to an Akamai edge hostname, ‘community.akamai.com.edgekey.net’, where the Akamai controlled edge server mapping takes over to assign the best available edge server. If you ‘[dig](https://en.wikipedia.org/wiki/Dig_(command))’ a hostname and see ‘edgekey.net’ then you know Akamai is being used by the content provider.

![Image](https://cdn-media-1.freecodecamp.org/images/tGhFH9LxM9izuNJab-6YGfSDfvdwD6weLNCt)
_Entering the Akamai network_

#### Akamai Interface

![Image](https://cdn-media-1.freecodecamp.org/images/CFgbmCCeyAd9V9tx7PsMr00nIGHBgiHB4SE1)
_Akamai’s [Luna Control Center](https://www.akamai.com/uk/en/solutions/intelligent-platform/control-center/" rel="noopener" target="_blank" title=") and Property Manager_

Akamai provides a web GUI named the ‘[Luna Control Center](https://www.akamai.com/uk/en/solutions/intelligent-platform/control-center/)’, several [APIs](https://developer.akamai.com/api/), and a [CLI](https://developer.akamai.com/cli).

As seen in the _Monitor_ tab, many reporting and analytics tools are available for generating insights at a CDN level. Logs from edge servers are also available on request.

In the _Configure_ tab we will focus on introducing Property Manager, and leave other options for a future post.

A _property_, sometimes also referred to as a _configuration_, is the main way to control how edge servers respond to user requests. Properties apply a list of _rules_ to a set of _hostnames_, and you can only apply one property at a time to any given hostname. Rules are made up of _criteria/match conditions_ and _behaviors_. An additional example of this will be seen later when looking at caching. Each property’s default rule must specify a valid _Content Provider_ (_CP) code_ to bill and report for the service. Rules are ‘last match wins’.

A Property Manager API (and [CLI](https://developer.akamai.com/legacy/cli/packages/property-manager.html)) exists, with a great [glossary of concepts](https://developer.akamai.com/api/core_features/property_manager/v1.html#papiconcepts).

When making changes to a property a new version is first created, allowing changes to be made and tested while the previous property remains active. The new version can be first activated on the Akamai staging network, that a developer can point their local machine to run tests against, before activating in production. Production activation takes roughly ten minutes to globally roll out the new version to all edge servers, with a fast fallback option rolling back within minutes.

#### Route Performance

In addition to providing an ever increasing amount of distributed edge servers, to be able to serve cached content from as close to every user as possible, the route to the content origin can be optimized. In Akamai’s case this is via [SureRoute](https://developer.akamai.com/legacy/learn/Optimization/SureRoute.html).

![Image](https://cdn-media-1.freecodecamp.org/images/AWcofYrlrbalUfaAe4iWIxe6IIFMHevRE4M8)
_SureRoute view of possible routes to the Content Origin_

Akamai’s network of servers (a user first connects to the edge server and any subsequent parent to that server) _overlays_ the default route to the origin. The default route may pass between several different ISPs and networks, which may not always peer well with each other. As seen above, a lossy link (or other such degradation) may mean a non-obvious route is the best option.

The best route is found in two steps.

* First, Akamai servers continually run probes against each other, and, at a lower rate, against all Akamai customer’s origins. These are used to calculate and distribute a centralized list of _candidate routes_ between each edge server/origin pairing.
* Secondly, to narrow down these raw candidate routes to a single best option, a static _SureRoute test object_ is placed by each customer at their specific origin of similar size to their average expected content. _Races_ to fetch this object are periodically ran between each edge server and the origin so that a record of that with the lowest latency and/or packet loss rate can be kept up to date.

This means that on every request to an edge server the fastest and most reliable route at that point in time can be used to reach the origin.

#### Caching

Caching at an edge server can greatly reduce latency for the end user.

As organizations scale caching can also become increasingly important to reduce load on the content origin for both better performance and to reduce costs.

As described in the answer given to “[Do Akamai edge servers share cached content](https://community.akamai.com/customers/s/question/0D50f00005RtpwrCAB/do-akamai-edge-servers-share-cached-content-or-go-to-origin?language=en_US)”, edge servers are grouped together into network ‘regions’. If a specific edge server’s cache is not populated it will send a local request to the other edge servers in its region and if a peer has content it will serve the response before caching it itself.

If all local peer’s caches are empty (or stale) then the request will be forwarded to the edge’s parent server, where the same local check will take place between the parent’s peers. If no content is cached along the entire route then it will return to the origin and repopulate the cache with its response.

![Image](https://cdn-media-1.freecodecamp.org/images/cl5Mskcs5NG0c-Cc1MHTY8KrRkjLb3Fmkgv5)
_Cache ID Modification behaviours_

The standard cache key used is made up of the host name (domain), path and query string. This can be modified to reduce cardinality and/or give more control over cache purging. This may be by only including specific query parameters, so excluding things such as product IDs, adding the values of certain cookies, headers, or user defined variables.

Match conditions (if ‘_x_’ cookie exists for example) can be combined with ‘bypass cache’ behaviors to create advanced scenarios such as caching different content for users with a session, or for users in different locations.

A browser extension such as [ModHeader](https://chrome.google.com/webstore/detail/modheader/idgpnmonknjnojddfkpgkljpfnnfcklj) can be used to view [Akamai Pragma Headers](https://community.akamai.com/customers/s/article/Using-Akamai-Pragma-headers-to-investigate-or-troubleshoot-Akamai-content-delivery?language=en_US) for investigating caching behavior locally.

#### Final thoughts

Using a CDN provides more control to content providers and tools such as those described above provide [benefits](https://www.akamai.com/uk/en/cdn/what-are-the-benefits-of-a-cdn.jsp) that are increasingly important when working at scale.

While Akamai specific products have been discussed here, similar concepts of working at scale exist with other CDN providers.

Other Akamai specifics may be covered in a future post, feel free to [keep an eye out](https://medium.com/@dfrase) or read up on suggested next topics such as:

* Security enhancements with [certificate](https://www.akamai.com/uk/en/solutions/intelligent-platform/secure-cdn.jsp) [management](https://developer.akamai.com/api/core_features/certificate_provisioning_system/v2.html) and Web Application Firewalls ([WAF](https://www.akamai.com/uk/en/resources/waf.jsp)s)
* [Image manager](https://developer.akamai.com/image-manager) for optimised image delivery
* [Cloudlets](https://developer.akamai.com/cloudlets) to provide granular control outside of the Property Manage activation cycle with many types available for different use cases
* Global Traffic Management ([GTM](https://www.akamai.com/uk/en/products/web-performance/global-traffic-management.jsp)) for DNS-based load balancing
* [mPulse](https://www.akamai.com/uk/en/products/web-performance/mpulse-real-user-monitoring.jsp) for utilising Real User Metrics (RUM) for performance monitoring

Thanks for reading ?

You may also enjoy:

* [A beginner’s guide to Amazon’s Elastic Container Service](https://medium.com/p/807d8c4960fd?source=user_profile---------11------------------)
* [How to incrementally add Flow to an existing React app](https://medium.freecodecamp.org/incrementally-add-flow-type-checking-react-261fee015f80)
* [Progressive enhancement with CSS Grid](https://medium.freecodecamp.org/progressive-enhancement-with-css-grid-8138d4c7508c)

