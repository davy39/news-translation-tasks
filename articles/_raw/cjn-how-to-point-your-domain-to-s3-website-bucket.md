---
title: How to Point your Domain to an S3 Website Bucket
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-21T00:08:34.000Z'
originalURL: https://freecodecamp.org/news/cjn-how-to-point-your-domain-to-s3-website-bucket
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/domain_name_point_to_s3_bucket.png
tags:
- name: dns
  slug: dns
- name: S3
  slug: s3
- name: Web Hosting
  slug: web-hosting
- name: website development,
  slug: website-development
seo_title: null
seo_desc: 'By Clark Jason Ngo

  If you''re hosting a static website in an S3 bucket and it''s your first time buying
  a domain name, this simple guide is for you.

  Summary - What You Need

  Amazon S3


  Have an S3 bucket with the same name as your domain name

  Upload your...'
---

By Clark Jason Ngo

If you're hosting a static website in an S3 bucket and it's your first time buying a domain name, this simple guide is for you.

## Summary - What You Need 

### Amazon S3

* Have an S3 bucket with the same name as your domain name
* Upload your website's code
* Allow public access
* Add a policy to enable S3 GetObject
* Enable static website hosting

### Domain Name provider

* In your domain name's DNS Zone settings, delete all **A** records
* In DNS Zone settings, add _www_ to **subdomain** and the S3 endpoint in hostname for **CNAME** records

Let's go through these steps one by one.

## Step 1: Create an S3 bucket

Create an S3 bucket to host your files for your website

First you need to create a bucket for your website. The name for your bucket must be the same as your domain name. Let's say we bought the domain name **www.clarkngo.net**. Then my S3 bucket's name should be **www.clarkngo.net** as well. 

After configuration, my endpoint should look similar to this:

http://www.clarkngo.net.s3-website-us-west-2.amazonaws.com

Go to your AWS console and login. Choose S3.

1. Click **Buckets**
2. Click **Create bucket**

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-119.png)

3. Add your domain name in the **bucket name**

4. You may choose any **Region**

### Creating the S3 bucket and general configuration

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-118.png)

Follow the checkboxes below and click **Create Bucket**.

Only tick the following:

* **Block public access to bucket and objects granted through _new_ access control lists (ACLs)**
* **Block public access to bucket and objects granted through _any_ access control lists (ACLs)**

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-120.png)

### Uploading files to the S3 Bucket

1. Click **Overview** and **Upload**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-121.png)

2. Upload your website files in **Select Files**

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-122.png)

3. For **Set permissions**, hit **Next**.

4. For **Set properties**, hit **Next**. (The default is Standard S3.)

5. For **Review**, hit **Upload**.

### Editing the Bucket Policy

1. Click **Permissions**, then **Bucket Policy**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-123.png)

2. Add the policy. (Note: For your website you'll change **arn:aws::s3:::www.clarkngo.net/***)

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-124.png)

```
{
    "Version": "2012-10-17",
    "Id": "Policy1548223592786",
    "Statement": [
        {
            "Sid": "Stmt1548223591553",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::www.clarkngo.net/*"
        }
    ]
}
```

3. Hit **Save**.

### Static website hosting

1. Click **Properties**, then **Static website hosting**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-125.png)

2. Choose **Use this bucket to host a website**.

3. For Index document, type _index.html_.

4. For Error document, type _index.html_.

5. Hit **Save**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-126.png)

## Step 2: Add the S3 Endpoint to your Domain

### Editing your DNS Zone

1. Login to your domain provider.
2. In this example, choose **Name Servers/DNS**, then **Modify DNS Zone** (or the equivalent).

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-127.png)

3. Remove all **A** records in your domain. Usually it will have a default IP address for a 404 Not Found page.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-128.png)

4. Add a **CNAME** to point to the S3 Bucket:

* add **www** for the Subdomain.
* add **www.clarkngo.net.s3-website-us-west-2.amazonaws.com** (the S3 Endpoint) to the Hostname.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-129.png)



And you're done! Note that it might take a while for your new settings take effect.

Connect with me in LinkedIn [here](https://www.linkedin.com/in/clarkngo/).

![Image](https://www.freecodecamp.org/news/content/images/2020/03/image-133.png)




