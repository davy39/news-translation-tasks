---
title: Will Cisco Be the Next Roadkill for AWS?
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2019-08-07T13:30:00.000Z'
originalURL: https://freecodecamp.org/news/will-cisco-be-the-next-roadkill-for-aws
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/cisco.png
tags:
- name: AWS
  slug: aws
- name: networking
  slug: networking
- name: virtualization
  slug: virtualization
seo_title: null
seo_desc: I’m not keeping very close track, but it feels like months since Amazon
  Web Services (AWS) most recently turned a major tech industry upside down. But with
  all their resources and market power, I’m sure there’s always something interesting
  cooking in...
---

I’m not keeping very close track, but it feels like months since Amazon Web Services (AWS) most recently turned a major tech industry upside down. But with all their resources and market power, I’m sure there’s always something interesting cooking in the kitchens of wherever Amazon’s headquarters happens to be right now.

So let me throw my purely speculative prediction into the silence. As I describe in my [Learn AWS in a Month of Lunches book](https://www.manning.com/books/learn-amazon-web-services-in-a-month-of-lunches?a_aid=bootstrap-it&a_bid=1c1b5e27&chan=medium), AWS has happily replaced your server room with EC2, your SAN and NAS with S3, your data warehousing with Redshift, and your database with RDS (and Aurora). They’ve also invented entirely new deployment models: politely informing you, for instance, that you simply have to serve your mobile apps via serverless functions (Lambda).

So what’s next? Well how about enterprise routing?

## What is enterprise routing these days?

![Image](https://www.freecodecamp.org/news/content/images/2019/08/image-18.png)

For decades, large organizations have controlled their internal network traffic with switches and routers configured by proprietary operating systems. The hardware is expensive (a single appliance can easily hit $10,000) and the cost of hiring the trained admins needed to maintain them can be much higher.

But is all that really still necessary?

These days your workloads are more likely to live in the cloud than in your actual office. Even in-house Internet of Things devices can easily be controlled from the cloud using, for instance, [AWS IoT](https://aws.amazon.com/iot/). I’m guessing that most modern on-premises enterprise routing involves controlling how people connect to production resources and to each other (email, VOIP, video) — but even that is more and more likely to be outsourced to SaaS solutions.

I may be missing something, but I just don’t see a compelling case for hardware switches here. Software-defined networking (SDN) should easily be up to the task. Why not just cover your campus in wireless access points, authenticate users using Kerberos or Active Directory, and configure your way to permissions/connectivity perfection.

## How AWS can rule the routing world?

Which brings me back to AWS. They’ve already got all the bases covered for authentication ([AWS Directory Service](https://aws.amazon.com/directoryservice/)) and high-end remote connectivity ([AWS Direct Connect](https://aws.amazon.com/directconnect/)). It probably wouldn’t take much for them to extend their networks to your campus. Perhaps they’d allow you to create local [VPCs](https://aws.amazon.com/vpc/) — complete with configurable subnets — that you’d use to organize your local infrastructure.

I’m imagining a company’s admin logging into the AWS Console to onboard a couple of new hires from marketing. They’d be added to an AWS IAM “Marketing” group that’s already got access to Amazon QuickSight dashboards and streaming data from your public-facing web servers running on EC2. But the group could just as easily be configured to allow its members into a database that, for regulatory reasons, must remain local.

What do you think? Are the days of the proprietary system network admin numbered?

_Looking for more? You might enjoy my_ [_books and Pluralsight courses_](https://bootstrap-it.com/) _on Linux, AWS, and Docker-related topics._

