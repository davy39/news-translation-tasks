---
title: Simple site hosting with Amazon S3 and HTTPS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-08T16:25:45.000Z'
originalURL: https://freecodecamp.org/news/simple-site-hosting-with-amazon-s3-and-https-5e78017f482a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*nKAE02IQZHWQ9oqNgGX3ag.jpeg
tags:
- name: AWS
  slug: aws
- name: Cloud Services
  slug: cloud-services
- name: S3
  slug: s3
- name: Web Development
  slug: web-development
- name: Web Hosting
  slug: web-hosting
seo_title: null
seo_desc: 'By Georgia Nola

  Hiya folks!

  In this tutorial I’ll show you how to host a static website with HTTPS on AWS with
  a custom domain. All this is possible using AWS free tier.

  However, the services we are going to use do incur some small charges. Generally...'
---

By Georgia Nola

Hiya folks!

In this tutorial I’ll show you how to host a static website with HTTPS on AWS with a custom domain. All this is possible using AWS free tier.

However, the services we are going to use do incur some small charges. Generally speaking these shouldn’t exceed $1/month.

We’ll be using a combination of the following AWS services:  
 —S3  
 — Route53  
 — Certificate manager  
— CloudFront

_Let’s get into it!_

### Setup your S3 buckets

First, you’ll need **two S3 buckets**, both should match your custom domain name with the second including the www subdomain.

Bucket 1: mywebsite.com  
Bucket 2: www.mywebsite.com

The first bucket (mywebsite.com) is the main bucket for your site. This contains all your files and assets for your static website.

![Image](https://cdn-media-1.freecodecamp.org/images/8tMXguNd0mEM-Kdt54Dy0WzMNvD0h0D0Moci)

Next we setup this bucket for static site hosting. You can find this under the Properties tab of the bucket, and we’re going to keep the defaults provided here with the index of the site set to index.html.

![Image](https://cdn-media-1.freecodecamp.org/images/-HHilv-8c1Y3OHdtaZhJR9DNlphJOBFd87gy)

We also need to make this bucket publicly accessible as a user’s browser will need to access the bucket’s files in order to render the website. We can do this by setting a Bucket Policy under the Permissions tab.

```
{       "Version": "2012-10-17",       "Statement": [        {            "Sid": "PublicReadGetObject",            "Effect": "Allow",            "Principal": "*",            "Action": "s3:GetObject",            "Resource": "MY_BUCKET_ARN"        }    ]}
```

This is a simple policy that will only allow public read access of objects in the bucket. Now, if you head to the endpoint defined in the static hosting config of the bucket, you should see your website.

![Image](https://cdn-media-1.freecodecamp.org/images/yEcjdf6UEr8iPVBjQCT0CtidDLpUQyhQCbLG)

Progress! But we can do better than that.

The second bucket (www.mywebsite.com) we will leave empty but configure to redirect to our first bucket using HTTP as the protocol (we’ll make it HTTPS later).

![Image](https://cdn-media-1.freecodecamp.org/images/MphGJGErSalxmf76wjQbOGSuyhg6y50dPWxT)
_Redirect requests back to the main bucket using HTTP protocol_

Your buckets are now ready to go!

### Configure Domains with Route53

So your website is up and running but only accessible via the bucket endpoint and not your custom domain. Let’s change that.

Head to **Route53**. If you’ve registered your domain with the Amazon Registrar you should see that a hosted zone has been setup for you with two record sets. One for Name Server (NS) and one for SOA.

All we need to do is to create two more record sets to point to the S3 bucket endpoints.

For each record set:  
 — Type: A — IPv4 address  
 — Alias: Yes  
 — Alias Target: the S3 website endpoint that matches what you set for Name.

![Image](https://cdn-media-1.freecodecamp.org/images/-pRXjHHB-EmOPzuTcNbKribluPQTsshaCGf-)
_Creating a record set for www subdomain_

Now we can head to the custom url…and voilà!  
We’re almost there, but there’s one last thing we’re missing…

![Image](https://cdn-media-1.freecodecamp.org/images/Tn5XmMFeKZDKn2zLITzmEfYtBOP6OH2ZSrVl)

**Note**: If your domain is registered with another domain registrar (not Amazon) you’ll need to follow some different steps to set this up. Usually you’ll need to add a CNAME record with a value of the main S3 buckets endpoint.

**Troubleshooting**:  
If you deleted the hosted zone Amazon created when you first registered the domain (I’ve done this because hosted zones do incur some charges), you’ll need to create a new hosted zone from scratch.

1. Select “Create Hosted Zone” and set the domain name, for example “mywebsite.com”
2. This will generate some new record sets for types NS and SOA.
3. Go into your registered domain and update the Name Servers values to those generated in the new NS record set.

### Requesting a Certificate

Awesome, the site is now hosted using the custom url! However we can only access it via HTTP protocol.  
We should always ensure our sites are secured using HTTPS protocol. This protects our site and users from malicious injection attacks and guarantees authenticity.

Head to **Certificate Manager** in AWS Console and request a new public certificate (this is free). You’ll be prompted to enter the domain names you wish to secure.

![Image](https://cdn-media-1.freecodecamp.org/images/nklZPz8lBuVETFkAxoKadUuDn3PLvztVIH3J)

Before the certificate can be issued, Amazon needs to be able to verify that you own the specified domains.

You can choose from two verification methods: Email or DNS.

Email is generally simpler, but you’ll need to ensure you can access the email used to register the domain. Alternatively, if you used Amazon Registrar and Route53, you can select the DNS method. This requires you to add some specific record sets to the hosted zone, but this is mostly automated for you so it’s quite simple.

It can take a few minutes for the certificate to be issued after validation.   
When its all done we can continue to the final step!

### Configuring CloudFront

For the final step we are going to use **CloudFront** which allows us to use the new SSL certificate to serve the website with HTTPS. CloudFront also speeds up the distribution of web content by storing it at multiple edge locations and delivering from the closest edge location to a user.

We need **two new web distributions**, one for each S3 bucket. Head to CloudFront in the AWS Console and create the first web distribution.  
There are lots of settings available to create a web distribution, but for the basics we only need to change five:

1. **Origin Domain Name**: Set this to the S3 website endpoint for one of the buckets. **Important**: This field will give you some auto-complete options with your S3 bucket names. However, using these can cause issues with redirecting to the bucket endpoint. So instead use the bucket endpoint directly.
2. **Origin Id**: This populated for you when you enter Origin Domain Name.
3. **Viewer Protocol Policy**: Set to “Redirect HTTP to HTTPS”.
4. **Alternate Domain Names**: This should match the name of the S3 bucket you’re pointing to. For example “mywebsite.com”.
5. **SSL Certificate**: Select “Custom SSL Certificate” and select your new certificate from the dropdown.

Do this again for the second S3 bucket.

![Image](https://cdn-media-1.freecodecamp.org/images/yAhOQRit35ON9mB7rtO4aefi6w2o9r-RQ2p1)

![Image](https://cdn-media-1.freecodecamp.org/images/AUfGClmx76ORz-sEOSipOFrJmBQE6KH2pDpf)

The distributions can take a while to spin up, so while we wait, let’s do the finishing steps.

Back in **S3**, go to your secondary bucket (www.mywebsite.com), in the Properties tab and under Static Website Hosting set the redirect protocol to HTTPS.

Finally, head back to **Route53**. We need to update the custom A records we created to now target the CloudFront distributions rather than the S3 buckets. For each record, change the Alias Target and select the CloudFront distribution available in the dropdown.

Note: Again, if you are using another DNS service you’ll need to go update the CNAME record from there to point to the CloudFront domain name.

![Image](https://cdn-media-1.freecodecamp.org/images/9PtEunXXDJGvAsXD03ZFepeSNosGtlXC-SWl)
_Huzzah!_

And there you have it! Your beautiful website is now available at the custom domain and served with HTTPS!

![Image](https://cdn-media-1.freecodecamp.org/images/1q28QH0CERJRnMkDZdrmOImMQD7szHNf5xZI)
_[From Giphy](https://giphy.com" rel="noopener" target="_blank" title=")_

Thanks for reading! I hope this guide was useful and enjoyable, I’d love to know if you found it helpful.

