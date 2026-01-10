---
title: How to launch a site on AWS for free in 15 minutes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-01T19:39:36.000Z'
originalURL: https://freecodecamp.org/news/how-to-launch-a-site-on-aws-for-free-in-15-minutes-7b3ce5d8d053
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FELQr_PxJW0CzDjdum9ysw.jpeg
tags:
- name: AWS
  slug: aws
- name: Front-end Development
  slug: front-end-development
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Daniel Simmons

  If you‘re completely new to Amazon Web Services (AWS), it can come across as soul-crushingly
  complicated.

  Not only does it seem like there’s a thousand different services to choose from,
  each of which has an equally cryptic name (li...'
---

By Daniel Simmons

If you‘re completely new to Amazon Web Services (AWS), it can come across as soul-crushingly complicated.

Not only does it seem like there’s a thousand different services to choose from, each of which has an equally cryptic name (like S3, Lambda, EC2, or Athena), but there is also **so** **much** to configure.

You’ve gotta decide how much memory to allocate to your functions, which geographic region of the world you want your code to be served from, and you have to build a weird JSON object in order to grant permissions? It’s REALLY easy to dip your toes in and decide it’s too confusing to get started.

If this describes your experience so far, then good — this article is for you.

I was in the exact same boat for longer than I’d care to admit.

But despite all of its daunting complexity, there is something about AWS that just keeps calling out to you.

There’s the speed, the reliability, even just the professional clout of being able to say that you have experience with AWS.

But, like with anything, if you want to get started, then you need to take the first step. So my goal in this article is to make that an easy one. I want to get you to the point that you can say “I have deployed a project on AWS.”

It will be much easier than you think, and it will give you a point from which to begin exploring AWS’s other services.

### Step 0: What you’ll need to follow along

The list is short, but I figured I’d put it front and center to make sure it’s clear from the beginning.

1. A working credit / debit card (don’t worry, it’s all free like the title says. But you will need to enter credit card info in order to create an AWS account)
2. Front-end code that you can upload and host on AWS. This can be as simple as an HTML document with `<p>Hello Wor`ld</p> in the body.

### Step 1: Make an AWS Account

![Image](https://cdn-media-1.freecodecamp.org/images/gHC1FuOPm-6n5bay5U83J-9jqyDXTuzvf5ud)

To be honest, I stopped at this point several times simply because it was one of those “free trial but they ask for your credit card info” situations, which I tend to resist on principle.

But the 12 month free tier is pretty amazing. A full year is a long time to be able to experiment on AWS before deciding whether it’s worth continuing to use it. (I am not in any way affiliated with AWS, just for the record).

So follow this link and create your account: [AWS Free Tier](https://aws.amazon.com/free/).

I know some people might have some concerns about the limitations on the free plan. For example, there is a monthly cap on GET and PUT requests (20,000 and 2,000 respectively), after which point you start getting charged.

But as long as you’re only using this to experiment and learn for now, there’s pretty much no chance of exceeding the limitations.

And even if you do, the pricing for exceeding the caps is typically fractions of a penny per 1,000 requests.

### Step 2: Create an S3 bucket for your project/site

To keep things as simple as possible, the only AWS service that we’ll be using for this project will be Simple Storage Service (or S3), one of Amazon’s cloud storage services.

S3 behaves a bit like Google Drive or Dropbox. But it can also be configured to serve files rather than just store them, which is what we’ll be doing.

Since we’ll just be serving files that are hosted on S3, this will be a static site, with no backend or connections to a database.

Now that you’ve got an AWS account, log in to the Management Console ([linked here](https://console.aws.amazon.com/)) and click on “Services” in the upper left of the main menu.

You’ll see that mind-bogglingly large list of service options that I mentioned in the beginning. Don’t worry about all that, just click on “S3” under the “Storage” section.

![Image](https://cdn-media-1.freecodecamp.org/images/IzizsR-GLeggIOxlGwlHn05wWUAim3P-onyx)

This will take you to the S3 page, where you can create different “buckets” to store your different projects.

Buckets are like folders on your desktop. But the document storage system on S3 does not follow the traditional folder structure ([more on that if you’re interested](https://serverfault.com/a/435828)). So instead,“bucket” seems to be the right word to use.

Click on the big blue button in the upper left called “Create Bucket” to create a bucket that will hold your project files.

![Image](https://cdn-media-1.freecodecamp.org/images/XkTs-DVcEFaFlTthSTzDpg3TJfZEvW4dh-SL)

![Image](https://cdn-media-1.freecodecamp.org/images/NJ00ZS1dYH4mX3x5iVPbrPOnhEpDJ-VShgJG)
_1) Select the region that is closest to you 2) The “tags” are just used for cost tracking. You don’t really NEED to fill this part out, but it’s a good practice_

![Image](https://cdn-media-1.freecodecamp.org/images/B0CIJCSOm2Fi9g39D-iihNjxmuegGbxtuFHk)

![Image](https://cdn-media-1.freecodecamp.org/images/wj0PsdPvkf1LccL6ckom3EN2hplFm3lyU7M-)

The main thing that you need to do here is make sure the public permissions are set to “Grant public read access to this bucket.”

You’ll get a warning from AWS, but don’t worry. They just want to make sure that no one could do this by accident. But this is exactly what you want to do.

Once you’re done, you’ll see your bucket in the list on your S3 console.

### Step 3: Add files & configure the settings on your bucket

Click on your newly created bucket in the list. This will bring you to a page where you can add contents to your bucket and configure its settings.

First, you’ll want to add your project files (mentioned at the beginning) on the “Overview” tab. Remember, these can be the files for any functioning front-end project.

You won’t be able to upload any folders (again, since S3 doesn’t actually have a folder structure). Instead, you’ll need to manually create any folders that you have in your project in S3 and upload your files to them.

![Image](https://cdn-media-1.freecodecamp.org/images/x7xUdptNB46x3R4UignuTPv-5qgrFdPPeDWK)

Next, click on the “Properties” tab.

This is where you’ll tell S3 that you want to use this bucket to host your files.

Just click on the tile that says “Static Website Hosting” and enter the names of your index (required) and error (not required) documents and you’re all done.

![Image](https://cdn-media-1.freecodecamp.org/images/teptTJ3QW-hsWlHBdM3VrkJAcT6TilzRlyX1)

![Image](https://cdn-media-1.freecodecamp.org/images/OMdIqlnvbQNtr58S1EZPvU3VgqiWDTdZLael)

Next, click on the “Permissions” tab.

You’ll see just below the main tabs that you start off in a subsection called “Access Control List”. This is already configured correctly, since you’ve already said that anyone should be able to read the files hosted in this bucket.

Now you’ll need to click on the “Bucket Policy” subsection. Here, you’ll be prompted to create a JSON object that contains the details of your bucket’s access permission policy.

![Image](https://cdn-media-1.freecodecamp.org/images/eaWfZ7lsITqJ3IYfbbA-fyjUtdpQyDmneGCE)

This part can be confusing. For now, I’ll just give you the JSON that will grant full public access to the files in your bucket. This will make the website publicly accessible.

Paste this into the bucket policy editor shown above:

```
{    "Version": "2012-10-17",    "Statement": [        {            "Sid": "PublicReadForGetBucketObjects",            "Effect": "Allow",            "Principal": "*",            "Action": "s3:GetObject",            "Resource": "arn:aws:s3:::YOUR-BUCKET-NAME/*"        }    ]}
```

Don’t forget to replace “YOUR-BUCKET-NAME” with… your bucket’s name.

### You’re done!

That’s it! You have now deployed a very simple static site on AWS S3.

To access your site, go back to the “Overview” tab on S3 and click on your index document (click on a blank area in the list item, not on the link to the document itself). You’ll get a slide-in menu on the right with a link to your site!

![Image](https://cdn-media-1.freecodecamp.org/images/ebm54zjdYMuQbAJD1-pqukLfabL2c9wx62SN)

![Image](https://cdn-media-1.freecodecamp.org/images/96pSOx3YuIYj-GDMN8OBJA3Y-lDmsDfS8LVt)

