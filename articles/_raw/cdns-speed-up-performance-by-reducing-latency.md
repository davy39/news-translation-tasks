---
title: How CDNs Help Speed Up Performance by Reducing Latency
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-06-27T00:17:23.000Z'
originalURL: https://freecodecamp.org/news/cdns-speed-up-performance-by-reducing-latency
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/pexels-pixabay-315934.jpg
tags:
- name: 'content delivery network '
  slug: content-delivery-network
- name: web performance
  slug: web-performance
seo_title: null
seo_desc: 'By Austin Gil

  In some recent tutorials, I covered supporting file uploads on the front end, supporting
  file uploads on the back end, and optimizing costs by moving file uploads to object
  storage.

  Today, I''ll continue to focus on more architectural wo...'
---

By Austin Gil

In some recent tutorials, I covered [supporting file uploads on the front end](https://austingil.com/uploading-files-with-html/), [supporting file uploads on the back end](https://austingil.com/file-uploads-in-node/), and optimizing costs by [moving file uploads to object storage.](https://austingil.com/upload-to-s3/)

Today, I'll continue to focus on more architectural work, but this time it’ll be focused on optimizing performance.

%[https://www.youtube.com/watch?v=Vymnxp-t0qs]

## Overview of Object Storage Solution

Let's say we have an application that stores uploaded files somewhere in the world. For this example, it’s an [Object Storage bucket from Akamai cloud computing services](https://www.linode.com/products/object-storage/), and I've deployed it to the `us-southeast-1` region.

You may be using a different provider and different region, but the following points will still apply.

So when I upload a cute photo of Nugget making a big ol’ yawn, I'll be able to access it at some URL like austins-bucket.us-southeast-1.linodeobjects.com/files/nugget.jpg

![Screenshot of my browser showing a cute photo of Nugget making a big yawn, and there's a box highlighting the URL from Akamai Object Storage.](https://austingil.com/wp-content/uploads/image-65-1080x608.png)

Nugget is a super cute dog. Naturally, a lot of people are going to want to see this. Unfortunately, because this photo is hosted in the `us-southeast-1` region, anyone that lives far away from that region has to wait longer before their eyes can feast on this beast.

Latency sucks.

And that’s why CDNs exist.

## What is a CDN?

CDN stands for "**content delivery network**". It’s a connected network of computers that are globally distributed and can store copies of the same files so that when a user makes a request for a specific file, it can be served from the nearest computer to the user. 

By using a CDN, the distance a request must travel is reduced. This helps resolve requests faster, regardless of a user’s location.

Here’s a [webpagetest.org test results](https://www.webpagetest.org/result/230417_BiDc3J_AP8/) for that photo of Nugget. The request was made from their servers in Japan, and it took 1.1 seconds for the request to complete.

![Image](https://austingil.com/wp-content/uploads/image-69-1080x723.png)

Instead of serving the file directly from my Object Storage bucket, I can set up a CDN in front of my application to cache the photo all over the world.

So users in Tokyo will get the same photo but served from their nearest CDN location (which is probably in Tokyo), and users in Toronto are going to get that same file, but served from their nearest CDN location (which is probably in Toronto).

This can have significant performance implications.

Let’s look at that same request, but served behind a CDN. The [webpagetest.org results](https://www.webpagetest.org/result/230417_BiDc41_ARJ/) still show the same photo of Nugget, and the request still originated from Tokyo, but this time it only took 0.2 seconds – **a fraction of the time!**

![Image](https://austingil.com/wp-content/uploads/image-68-1080x956.png)

When the request is made for this image, the CDN can check if it already has a cached version. If it does, it can respond immediately. If it doesn’t, it can go fetch the original file from Object Storage, then save a cached version for any future requests.

**Note**: the numbers reported above are from a single test. They may vary depending on network conditions.

## The Compounding Returns of CDNs

The example above focused on improving delivery speeds of uploaded files. In that context, I was only dealing with a single image that is uploaded to an Object Storage bucket. It shows almost a full second improvement in response times, which is great, but things get even better when you consider other types of assets.

CDNs are great for any static asset (CSS, JavaScript, fonts, images, icons, and so on). By putting it in front of my application, all the other static files can automatically get cached as well. This includes the files that Nuxt.js generates in the build process, and which are hosted on the application server.

This is especially relevant when you consider the “[Critical rendering path](https://developer.mozilla.org/en-US/docs/Web/Performance/Critical_rendering_path)” and render-blocking resources like CSS, JavaScript, or fonts.

When a webpage loads, as the browser comes across a render-blocking resource, it will pause parsing and go download the resource before it continues (hence “render-blocking”). So any latency that affects a single asset may also impact the performance of other assets further down the network cascade.

This means the performance improvements from a CDN are compounding. Nice!

So is this about showing cute photos of my dog to more people even faster, or is it about helping you make your applications run faster? YES!

Whatever motivates you to build faster websites, including a CDN as part of your application infrastructure is a crucial step if you plan on serving customers from more than one region.

## How to Connect Akamai CDN to Object Storage

Now I want to take a little side-quest and share how I set up Akamai with Object Storage. I didn’t find much information on the subject, and I’d like to help anyone in this specific situation. If it doesn’t apply to your use case, feel free to skip this section.

With something like 300,000 servers across 4,000 locations, Akamai is the largest CDN provider in the world. It’s used by some of the biggest companies in the world, but it’s hard to find Akamai-related content because most large companies don't like to share unnecessary information about their infrastructure.

But I'm not most companies :)

(Note: You will need an Akamai account and access to your DNS editor)

In the [Akamai Control Center](https://control.akamai.com/), I created [a new Property](https://control.akamai.com/apps/create/#/property/products) using the [Ion Standard product,](https://www.akamai.com/products/web-performance-optimization) which is great for general purpose CDN delivery.

![Image](https://austingil.com/wp-content/uploads/image-71-1080x274.png)

After clicking “Create Property”, you’ll be prompted to choose whether to use the setup wizard to guide you through creating the property, or you can go straight to the Property Manager settings for the new property. I chose the latter.

In the Property Manager, I had to add a new hostname in the Property Hostnames section. I added the hostname for my application. This is the URL where users will find your application. In my case, it was uploader.austingil.com.

![Image](https://austingil.com/wp-content/uploads/image-76-1080x520.png)

Part of this process also requires setting up an SSL certificate for the hostname. I left the default value selected for Enhanced TLS.

![Image](https://austingil.com/wp-content/uploads/image-77-1080x520.png)

With all that set up, Akamai will show me the following Property Hostname and Edge Hostname. We’ll come back to these later when it’s time to make DNS changes.

* **Property Hostname:** uploader.austingil.com
* **Edge Hostname:** uploader.austingil.com-v2.edgekey.net

![Image](https://austingil.com/wp-content/uploads/image-72-1080x155.png)

Next, I had to set up the actual property’s behavior, which meant editing the Default Rule under the Property Configuration Settings. Specifically, I had to point the **Origin Server Hostname** to the domain where my origin server will live.

![Image](https://austingil.com/wp-content/uploads/image-73-1080x761.png)

In my DNS, I created a new A record pointing origin-uploader.austingil.com to my origin server’s IP address, then added a CNAME record that points uploader.austingil.com to the Edge Hostname provided by Akamai.

* A: origin-uploader.austingil.com -> origin server IP
* CNAME: uploader.austingil.com -> uploader.austingil.com-v2.edgekey.net

This lets me build out my CDN configuration and test it as needed, only sending traffic through the CDN when I’m ready.

Finally, to serve files in my Object Storage instance through Akamai, I created a new rule based on the blank rule template. I set the rule criteria to apply to all requests going to the `/files/*` sub-route.

![Image](https://austingil.com/wp-content/uploads/image-74-1080x402.png)

The rule behavior is set up to rewrite the request’s Origin Server Hostname and change it to my Object Storage location: npm.us-southeast-1.linodeobjects.com.

![Image](https://austingil.com/wp-content/uploads/image-75-1080x602.png)

This way, any request that goes to [uploader.austingil.com/files/nugget.jpeg](https://uploader.austingil.com/files/nugget.jpg) is served **through** the CDN, but the file originates from the Object Storage location. And when you load the application, all the static assets generated by Nuxt are served from the CDN as well. All other requests are passed through Akamai and forwarded to origin-uploader.austingil.com, which points to the origin server.

So that’s how I’ve configured Akamai CDN to sit in front of my application. Hopefully, it all made sense, but if you have questions, feel free to ask me.

## To Sum Up

Today we looked at what a CDN is, the role it plays in reducing network latency, and how to set up Akamai CDN with Object Storage.

But this is just the tip of the iceberg. There’s a whole world of tweaking CDN configuration to get even more performance. 

There are also a lot of other performance and security features a CDN can offer beyond just static file caching: Web Application Firewalls, faster network path resolution, [DDoS protection](https://www.akamai.com/solutions/security/ddos-protection), bot mitigation, [edge compute](https://www.akamai.com/solutions/edge), automated [image and video optimization](https://www.akamai.com/products/image-and-video-manager), malware scanning, request security headers, and more. 

My colleague [Mike Elissen](https://www.linkedin.com/in/mikeelissen/) also covers some great security topics [on his blog](https://blog.securitylevelup.eu/).

The most important thing that I wanted to convey today is that using a CDN improves file delivery performance by caching content close to the user.

Thank you so much for reading. If you liked this article, and want to support me, the best ways to do so are to [share it](https://twitter.com/share?via=heyAustinGil), [sign up for my newsletter](https://austingil.com/newsletter/), and [follow me on Twitter](https://twitter.com/heyAustinGil).

_You can find this and my other articles published on [austingil.com](https://austingil.com/file-uploads-cdn/)._

