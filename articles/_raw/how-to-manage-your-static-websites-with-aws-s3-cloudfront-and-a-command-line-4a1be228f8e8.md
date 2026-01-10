---
title: How to manage your static websites with AWS S3, CloudFront, and a command line
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-09-14T00:17:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-manage-your-static-websites-with-aws-s3-cloudfront-and-a-command-line-4a1be228f8e8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*zxIISvYq2_dz4R3THj17pA.jpeg
tags:
- name: AWS
  slug: aws
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Ben Cheng

  Here’s a short list of things you shouldn’t need to worry about when setting up
  a static website:


  scaling up your servers for surges in traffic

  logging into the AWS Management Console just to upload a new index.html file

  spending US$5 t...'
---

By Ben Cheng

Here’s a short list of things you shouldn’t need to worry about when setting up a static website:

* scaling up your servers for surges in traffic
* logging into the AWS Management Console just to upload a new index.html file
* spending US$5 to host a single static website

I myself was sick of worrying about these things. So I learned some Go, developed a small command line tool over the weekend, and open-sourced it.

[AWS S3](https://aws.amazon.com/s3) is an affordable option for for hosting (and free for first time users), and AWS [CloudFront](https://aws.amazon.com/cloudfront/) is good for CDN. But setting up the two is a pain. The checklist is pretty long:

1. set up S3 correctly
2. configure CloudFront
3. make sure you’ve followed best practices such as HTTP -> HTTPS redirection
4. sync files
5. invalidate CloudFront for updates.

Luckily, my open source [AWS-site-manager](https://github.com/oursky/aws-site-manager) makes hosting and updating a static site as simple as a single command line.

AWS Site Manager is a simple command-line tool that makes it easy to host a static website with AWS S3 and CloudFront, without running afoul of best practices.

If this is your first time hosting a site, create an AWS account and register your domain name with a service such as [Namecheap](https://www.namecheap.com/) (make sure you use their monthly discount coupon).

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZcHHO4Em6dZ7FA87kM4j3g.png)

### Why use S3 and CloudFront for static sites?

So given all the trouble, why bother with S3 and CloudFront? The two main reasons are:

1. Affordability for features (compared to free Heroku dyno — which shuts down when you reach their inactivity limit — or Github.io — which doesn’t support HTTPS with custom domains)
2. Speed (CloudFront is a cheap, but acceptable CDN)

Given the advantages, the only barrier was the setup, so we created a command line tool for convenient future usage. Below, I’ll walk you through how to set up this open-source site manager.

### [AWS-site-manager](https://github.com/oursky/aws-site-manager) does 2 things:

#### 1. Setup S3 and CloudFront with an opinionated configuration:

* Create S3 buckets
* Configure CloudFront Distribution and set up CNAME
* Upload and set custom HTTPS certs
* Redirect www to naked domains for better SEO
* Redirect HTTP to HTTPS for better SEO (if HTTPS is enabled)
* _Set up IAM / let’s encrypt cert automatically (coming soon)_

#### 2. Sync a local folder with S3

* Gzip files for better site speed _(will replace with CloudFront Gzip Setting)_
* Sensible default for HTTP Header (correct MIME type, max-age=900, etag etc)
* Invalidate CloudFront distribution for files synced

### Getting started: Install

Download the binary for Linux / Mac / Windows [release here](https://github.com/oursky/aws-site-manager/releases/).

Or compile from sources: If you have [Go 1.6 or above installed](https://golang.org/dl/), run the following command:

### **How to Use AWS Site Manager**

#### 1. Set up AWS Credentials and config.

If you haven’t set up AWS credentials on your environment before, you can set it up by putting the following lines in `~/.aws/credentials`.

And in `~/.aws/config`

You should also set the environment variable of AWS_SDK_LOAD_CONFIG  
 If you’re on Linux / Mac using bash put the following line in `~/.bashrc`

You can read more about AWS CLI set up on its [official documentation](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html).

#### 2. Use it!

Assuming you’re going to set up a website example.com and [www.example.com,](http://www.example.com,) you can:

The commands above will:

* set up a S3 bucket example.com and [www.example.com](http://www.example.com)
* sync all files in local folder
* redirect [www.example.com](http://www.example.com) to example.com

If you want to use https, and have the cert in PEM format ready, run the following command lines instead to setup HTTPS. (if your SSL registry sent you `.key` / `.crt`, [read this](http://stackoverflow.com/questions/991758/how-to-get-an-openssl-pem-file-from-key-and-crt-files))

Finally, you need to set up DNS mapping to your CloudFront distribution endpoint. Consider using AWS [Route-53](https://aws.amazon.com/route53/) for that.

You need to setup a CNAME record to point your domain name to the Cloud Front Distribution. You can get your CloudFront Domain Name from AWS Management Console, then set your domain’s CNAME to the Domain Name.

![Image](https://cdn-media-1.freecodecamp.org/images/1*TGXROtf37r5f-_ysbdornQ.png)

If you need to update the site, just run `aws-site-manager sync –domain example.com` In the folder and the command will compare the file changes, upload new files to S3, and invalidate the CloudFront cache for you.

### Go forth and launch

This project solved a recurring problem for me and my team at [Oursky](https://github.com/oursky). In addition to building mobile and web apps, we also often create one-off static sites that we want to be able to conveniently update every once in a while.

[AWS-site-manager](https://github.com/oursky/aws-site-manager) is open source and in its preliminary stages. If you want to contribute, you can create issues or submit a pull request.

If you have any questions about this project or serverless solutions in general, you can contact me here or on [Twitter](https://twitter.com/chpapa). Or, if you’re ever dropping by Hong Kong, come visit my office for a chat!

Enjoy!

PS: My company’s also working on another open-sourced project called [Skygear.io](http://www.skygear.io/), which is a free BaaS that includes features such as chat, social networks, bots, social logins, real-time and offline data sync, CMS for mobile, user management, etc.

