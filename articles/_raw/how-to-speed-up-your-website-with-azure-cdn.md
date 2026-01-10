---
title: How to Speed Up Your Website with Azure CDN
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-26T15:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-speed-up-your-website-with-azure-cdn
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/cdn-cover.jpg
tags:
- name: Azure
  slug: azure
- name: 'content delivery network '
  slug: content-delivery-network
- name: Microsoft
  slug: microsoft
- name: web performance
  slug: web-performance
seo_title: null
seo_desc: 'By Arjav Dave

  What is a CDN?

  A Content Delivery Network (CDN) helps you deliver your content more quickly. You
  can serve any type of content that remains unchanged over a period of time, like
  images, videos, CSS, JavaScript, HTML files, PDFs, and mor...'
---

By Arjav Dave

## What is a CDN?

A Content Delivery Network (CDN) helps you deliver your content more quickly. You can serve any type of content that remains unchanged over a period of time, like images, videos, CSS, JavaScript, HTML files, PDFs, and more. 

A CDN is a group of servers that are spread across the world to deliver the content from the _Edge servers_. Edge servers are servers located closest to the place from where the request is being made. 

Depending on the request, edge servers may either return the content from its cache or they can fetch it from the _Origin Server_. The servers that serve the actual content are called Origin servers.

![CDN Overview](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/0i7t9e95tryv3mi44ghc.png)

In the above image, the Edge Servers are located around the world and the Origin Server is located in California, USA. When a request is made, the Edge Server located at Mumbai, India may contact the Origin Server if it's not able to serve the content.

## How Does a CDN Work?

CDNs have four main parts: a Consumer, a DNS, an Edge Server, and an Origin Server.

![CDN Detail](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/gni65528kxlmciivhnyw.png)

When the Consumer makes a request, it is at first accepted by its Internet Service Provider (ISP). The ISP will then hit the content provider's _Authoritative DNS_.

> An Authoritative DNS converts the DNS request to an IP request.

When the Authoritative DNS is made, it returns the IP address of the closest Edge Server. The Edge Server will then check in its own cache to see if the requested content is available. 

If it is, then it returns the content. If the content is not available, it requests the content from the Origin Server and on retrieval caches it.

## Benefits of a CDN

### Low Bandwidth Consumption

Many web hosts have a limited bandwidth allocation per month. If you go beyond that you will be charged extra. 

With a CDN most of your bandwidth will be saved since the content will be served by the edge servers.

### Low Latency

The Edge Servers cache the content. So anytime cached content is requested the latency is reduced drastically. This is because the request doesn't go all the way to the Origin Server.

### Security against DDoS

Almost all the popular CDN's have the capability to protect your webserver against Distributed denial of service (DDos) attacks.

### Improves SEO

Loading time is one of the factors that can affect your site's SEO rankings. If you are serving most of your content via CDN, the loading times are drastically reduced and can help improve your SEO.

## Deep Dive into Azure CDN

Let's say you have created an Azure Storage Account and hosted a very simple site that displays Hello World as h1. Now that you know the benefits of CDNs, you want to serve your simple site over CDN. 

You will have an endpoint like _[https://demostorageaccountarjav.z29.web.core.windows.net/](https://demostorageaccountarjav.z29.web.core.windows.net/)_ (where instead of demostorageaccountarjav it would be your storage account's name). Here are more details on how to [setup a static website](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blob-static-website).

Login to your Azure Portal and click on _Create a resource_ from you dashboard. Search for _CDN_ which will open the resource in the marketplace as below.

![CDN Create Resource](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ravgtt3j0xmeu5osd9d2.png)
_Create CDN_

This will open up a form to create a CDN profile. A CDN profile is a set of CDN endpoints. There is not much to fill in here except the name, resource group, and the pricing tier.

Next, select the checkbox to create a CDN endpoint. An endpoint is where the Consumer will be requesting content. So if you have multiple sites you can create multiple endpoints as well.

I have attached a screenshot for your reference on what values to put in. Since CDN is a global service the region selection will be disabled.

![CDN Details](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/z35xu3l7ox243ea6ecfj.png)
_CDN Details_

You can now click on _Create_ to generate the profile and endpoint. It will take a couple of minutes to create. After it is created and when you go to the home screen, you will have these 4 resources:

![Azure Resources](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/o6bxldg59sqod68o4kq1.png)
_Azure Resources_

As discussed earlier, the CDN Profile is a group of _Endpoints_. To view the details click the *_Endpoint_ resource. You will see an overview with a link to the _Endpoint hostname_.

![Endpoint Overview](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/vt4t5uxyv6u0i5llicwp.png)
_Endpoint Overview_

When you open the endpoint hostname it might show "404 not found" initially. You might have to wait another 10-15 minutes before your actual site is visible.

As discussed in the [benefits](#heading-benefits-of-a-cdn) section you can configure the Endpoint for security, caching, routing, and a lot of other things. You can explore more options [here](https://docs.microsoft.com/en-us/azure/cdn/cdn-how-caching-works).

## How to Access via SAS Token

You may be wondering what to do if your resource is in a private container and can only be accessed via a _Shared Access Signature_ (SAS) Token. Well you are in luck! The query strings are passed on as they are and since SAS is as a query string you are good.

Go ahead and create a new storage account (with static website disabled). Add a new Endpoint in the CDN profile that points to the newly created storage account.

For demo purposes I have created a container named _site_ with private access level. And I've uploaded a Blob to it named _Photo.jpeg_ in a Storage Account with the URL [https://demostorageaccountarjav.blob.core.windows.net](https://demostorageaccountarjav.blob.core.windows.net).

You can of course get a SAS token from the Azure portal directly for testing, but that's not how you would usually do in the real world. For that, you'll find below a simple snippet to create a SAS token in Node.js.

```
const azureSasToken = require('azure-sas-token');
 
// default token validity is 7 days
let sasToken = azureSasToken.createSharedAccessToken('https://<service namespace>.servicebus.windows.net/<topic name or queue>',
                                '<signature key name>',
                                '<signature hash>');
console.log(`sasToken: ${sasToken}`);
 
// Specify your own validity in secs, two hours in this example
sasToken = azureSasToken.createSharedAccessToken('https://<service namespace>.servicebus.windows.net/<topic name or queue>',
                                '<signature key name>',
                                '<signature hash>', 
                                60 * 60 * 2);
console.log(`sasToken: ${sasToken}`);

```

We have used a simple npm package named [azure-sas-token](https://www.npmjs.com/package/azure-sas-token). Once the SAS is generated your URL will look something like this:

```
https://demostorageaccountarjav.blob.core.windows.net/site/Photo.jpeg?sp=r&st=2021-03-25T07:28:45Z&se=2022-02-02T15:28:45Z&spr=https&sv=2020-02-10&sr=b&sig=PD4HlRI8bDEirMevpYQgpx6drwh%2BE5EpILfXkQOMlvw%3D

```

The above URL is pointing directly to the storage account. So go ahead and change the origin so that it uses the origin endpoint.

```
https://demowebsitearjav.azureedge.net/site/Photo.jpeg?sp=r&st=2021-03-25T07:28:45Z&se=2022-02-02T15:28:45Z&spr=https&sv=2020-02-10&sr=b&sig=PD4HlRI8bDEirMevpYQgpx6drwh%2BE5EpILfXkQOMlvw%3D

```

When you visit this site you will now be able to view the protected resource via CDN. You might have to wait a few minutes and/or purge your Endpoint to see the updated content.

## Conclusion

In my opinion everyone should be using a Content Delivery Network. There are lots of other providers like Cloudflare, S3, and so on. But Microsoft is one of the major players emerging with a wide variety of services. 

If you are an Azure fan like I am, you should definitely give Azure CDN a try.

For any feedback or questions you can get in touch with me.

Check [here](https://arjavdave.com) for more tutorials like this.

