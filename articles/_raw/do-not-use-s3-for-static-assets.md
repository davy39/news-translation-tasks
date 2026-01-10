---
title: Why You Shouldn’t Use AWS S3 or CloudFront to Deliver Static Assets
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-01T00:20:00.000Z'
originalURL: https://freecodecamp.org/news/do-not-use-s3-for-static-assets
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ab0740569d1a4ca271f.jpg
tags:
- name: AWS
  slug: aws
- name: S3
  slug: s3
seo_title: null
seo_desc: "By Mehul Mohan\nAWS is THE cool kid in the town. Every comparison of different\
  \ cloud providers is incomplete unless you compare them with AWS at least once.\
  \ \nBut S3, the most popular solution for storing on the cloud and the one everyone\
  \ loves, should..."
---

By Mehul Mohan

AWS is THE cool kid in the town. Every comparison of different cloud providers is incomplete unless you compare them with AWS at least once. 

But S3, the most popular solution for storing on the cloud and the one everyone loves, should not always be your choice. In this article, I'll explain why.

_**Note:** Please don't immediately yell at me about how and why AWS is best. I know they are at the top of cloud computing - and in no way am I trying to target any of their business practices and services._   
  
_I've just used CloudFront + S3 myself, along with DigitalOcean + Cloudflare too, and have laid down my observations. Please take my thoughts constructively, and if you think I've made any mistakes, tweet me at [mehulmpt](https://twitter.com/mehulmpt)._

## CloudFront + S3

CloudFront is another service often used (and recommended) with S3 when you're trying to distribute files digitally all over the globe. CloudFront is a CDN from Amazon with edge servers all over the world. This is how it works:

Your user, say from India, tries to load your website whose server is located in the USA. Let's say you're using a SPA like React or Angular. The first index.html page will load from your origin server (it is usually a good practice to never cache HTML pages, especially if you're using SSR applications to prevent cache mishaps). 

After that, if you've hosted your JS/CSS files on CloudFront (S3), those calls will be made to a domain name from CloudFront which resolves to an IP address of a machine closest to your location. In this case, it's probably some server from AWS sitting in some data center in Mumbai, India.

From this point, that server has the responsibility of delivering that file. Two things can happen:

* your file is already available with that Mumbai server (cached), and that server returns you that file immediately (cache hit), 
* or it does not has that file and has to perform a trip to your origin server (S3 bucket in this case) to get that file.

But even if there's a cache miss, chances are high that it will be still faster for a user compared to not having CloudFront in front. 

Why? Because when there is a cache miss and the edge server is trying to reach the main server, it is using a Tier 1 internet connection line operated by Amazon - a trillion-dollar US company. They likely have much better internet connectivity and latency than what your ISP can offer. 

Also, because they're on the same global Amazon network, they can do some neat optimizations to save more time.

Alright! Sounds great to me so far, so what's the problem? Hold your horses, we'll get to it.

# Asset compression

CloudFront allows you to deliver compressed assets using GZIP. But there's even a cooler kid in the market: brotli compression. And it is supported by almost every major browser. 

Brotli compresses your transmission data even more. This means it's not only good on your wallet, but it's also good for the end-user (because they'll spend less time seeing that loading/white screen).

Amazon CloudFront does not support brotli compression delivery, yet. And I won't blame them for this either. This is because brotli compression is slow to do on the fly (CloudFront does gzip on the fly), so they have not implemented it yet.

Sure, then let's do it ourselves and store it on S3 and deliver the compressed version, right? Unfortunately, it is not as simple, and we'll soon spin down into more of an architecture problem.

A typical asset URL would look like this: http://mysite/assets/javascript/file.js

When your browser makes a request, it sends a header: Accept-Encoding. This header can contain compression algorithms your browser can support, like gzip, deflate, brotli, etc. The server now has to act smart to have maximum efficiency.

1. If the client supports brotli, then always deliver the brotli compressed asset.
2. If the client supports gzip, then always deliver gzip.
3. Otherwise, deliver the original file.
4. Also, make sure that in the response type, the correct Content-Encoding is set so that browser can recognize the compression algorithm.

Now, firstly, you have to create 3 variants of every single asset file:

1. file.js
2. file.js.br - brotli
3. file.js.gz - gzip

And you have to _conditionally_ deliver them depending on if the browser supports it or not. CloudFront is a "dumb" CDN - it will just map your request URL to the file on your server. It cannot perform any transformations unless.... you opt-in for another AWS service - Lambda@edge functions

We all likely know what Lambda is on AWS - you can run functions on the cloud without worrying about underlying infrastructure upscaling or downscaling. Per API request pricing, time-bounded, sweet. Lambda@edge is a similar service but was made for edge servers (CloudFront CDN datacenters)

You can technically configure a Lambda server to act as a "middle man" between the request made by your client and the CloudFront CDN. Lambda can open the request, see the supported content headers, modify the URL accordingly and forward it to the "dumb" CloudFront which is going to retrieve the modified URL file then. 

For example, if Lambda sees that browser sent an Accept-Encoding: br then lambda can be used to modify the request URL from /javascript/file.js to /javascript/file.js.br without actually telling the user side. Cloudfront will now retrieve a smaller payload and return a response for a brotli encoding. WIN!

But that is good, isn't it? WHERE is the problem? The problem is... pricing.

## AWS is ridiculously expensive (for this task)

Whatever you've done so far sounds and looks very good. But when you look at what's happening when you start to hit significant numbers, you'll realize that AWS isn't great when it comes to data transfer. [Zoom just bounced AWS for the same reason](https://www.lastweekinaws.com/blog/why-zoom-chose-oracle-cloud-over-aws-and-maybe-you-should-too/). 

Plus, with the asset compression, now you also have to pay for Lambda@edge calls. I figured out that implementing Lambda@edge will actually reduce your costs, otherwise you'll pay much more for AWS for traffic!

CloudFront works on data transfer pricing. It does not charge you when it retrieves data from the S3 bucket, it charges you when a user retrieves data from the edge servers.

## Upper cost bound

In the most expensive country - India - CloudFront charges you $0.170 per GB of data transferred. This is huge! 

Let's say you have a popular (mainly) Indian website with about 50,000 users visiting your site daily. Also, let's say you make some design changes every week on your site (pretty common for fast iterating products) so you have to invalidate the browser and CloudFront cache.

Also, let's assume on average, a single user downloads about 10MB of the static asset from your site (includes CSS/JS/images/fonts) hosted on S3 proxied through CloudFront.

Let's calculate the cost:

1. 50K Indian users
2. 0.17 USD per GB
3. 10MB per user
4. Every user retrieves this 4 times a month (you flush your cache 4 times - once every week)

Cost = 50000 * 0.17 * (10/1024) * 4 = 332 USD. That is your COST of just data transfer! I did not calculate the S3 storage cost and the hosting site cost. (I also did not include lambda pricing because it's not much => $(0.20 * (50,000 * 4))/1 million = 4 cents.)

## Lower cost bound

In this case, let's assume a US based traffic site. The parameters now would be:

1. 50K USA users
2. 0.085 USD per GB
3. 3 MB per user
4. Every user retrieves this 4 times a month (you flush your cache 4 times - once every week)

The cost = 50000*0.085*3*4/1024 = 50 USD. That is the lowest you'll pay when using CloudFront with the mentioned traffic (given that all of your 50K users are from the USA only). And remember, that is the cost only for the data transfers! (Not including server costs for hosting your website.)

## Alternative

Let's say now you host all these static assets on your main server only - reverse proxied by NGiNX and say, running on a $60 DigitalOcean instance.

Your data transfer per month = 50000 * (10/1024) * 4 = 1952 GB approximately 2TB - DigitalOcean covers your 1TB of transfer per droplet for free. And it is $10 per 1TB from then, so it'll be $70 net for running the server.

Sure, you'll get some latency now - because you're hosting it yourself (we'll even fix this later). NGiNX is a high performing web server and you can rely on it not to be a bottleneck in your static asset delivery. 

So you just dropped the cost of "only asset transfer" from $332 to $70 for running the whole server! Bonus tip? We were focusing on running this only in India, so use a DigitalOcean server from India. This would mean less latency.

Not only this, but you can also opt for Cloudflare CDN too - which is FREE. Cloudflare won't respect your files to keep in the CDN if they're too big or too infrequently accessed. But we're assuming a hell of a popular site here, so we should be fine. If not, opt for any other CDN service, and I guarantee you it will be less than $332 a month.

TL;DR - If you're hosting a website with medium-large amounts of traffic with regularly scheduled updates, it is much more cost efficient to host assets yourself and use external CDNs (or even things like DigitalOcean CDN) instead of using S3 and CloudFront (where data traffic rates are through the roof).

## Conclusion

I used this setup (CloudFront + AWS S3) on [codedamn.com](https://codedamn.com) - a platform for developers to learn and grow. I soon realised that although it looks fancy and I've put codedamn into the big leagues - Amazon - it's just not efficient enough. 

Do you agree with me? What do you think? Let me know by [tweeting at me on my Twitter](https://twitter.com/mehulmpt) or reaching out to me on [Instagram](https://instagram.com/mehulmpt).

Peace!

