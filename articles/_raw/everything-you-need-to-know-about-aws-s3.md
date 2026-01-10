---
title: Everything You Need to Know About AWS S3
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2020-08-10T20:25:33.000Z'
originalURL: https://freecodecamp.org/news/everything-you-need-to-know-about-aws-s3
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-10-at-6.26.31-PM.png
tags:
- name: AWS
  slug: aws
- name: S3
  slug: s3
- name: Security
  slug: security
- name: storage
  slug: storage
seo_title: null
seo_desc: 'This article will provide an in-depth introduction to AWS S3 — the secure,
  scalable, and super cheap storage service from Amazon Web Services.

  If you have ever worked as a developer, you have likely come across file storage
  use cases. From simple ima...'
---

This article will provide an in-depth introduction to AWS S3 — the secure, scalable, and super cheap storage service from Amazon Web Services.

If you have ever worked as a developer, you have likely come across file storage use cases. From simple images to large videos, uploading, storing, and accessing those files when you need them is always tricky.

The usual answer to file storage is to keep them on the same server where you host your web applications. But with the advent of serverless architectures and single-page applications, storing files on the same server is not a good idea.

You could argue that you can store files in databases. But trust me, it won’t be a pleasant experience.

So what's another option?

## What is S3?

Let's look at AWS S3. S3 is an easy-to-use, scalable, and cheap storage service from Amazon. You can use S3 to store any amount of data for a wide range of use cases.

Static website hosting, data archival, and software delivery are a few general scenarios where S3 would be a perfect tool. 

You can easily push and pull data with S3 using the AWS SDK. S3 also supports a number of popular programming languages, so you can use your existing stack and integrate S3 pretty easily.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-10-at-6.14.06-PM.png)
_AWS Console_

S3 also offers a great user interface via the [AWS console](https://aws.amazon.com/console/). You can use it to view the data pushed to S3 along with additional options such as security and version control.

### Buckets

In S3, files are stored in buckets. Buckets are similar to folders on your computer.

Every bucket has its own unique name which can be used only once. For example, if there is a bucket called “freecodecamp”, neither you nor anyone else can re-use the same bucket name.

This is useful to uniquely identify resources and for static website hosting with domain names.

There are no limits on the number of files you can store in a bucket. Buckets also provide additional features such as version control and [policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html).

You can also use different buckets for a single application. For example, an app that stores medical records can use two buckets: one for private customer data and another public bucket that contains whitepapers.

S3 is also an object-based storage service which means S3 considers each file an object. Every object can have its own metadata that includes the name, size, date, and other information.

## S3 Storage Types

S3 has three storage classes based on general use cases.

### S3 Standard

S3 Standard is the default storage plan you will be put into when you start using S3. The standard storage class has excellent performance, durability, and availability. 

S3 Standard is best if you have data that you have to access frequently.

### S3 Infrequent Access (S3-IA)

S3 Infrequent Access offers a lower price for data compared to the standard plan. You can use S3-IA for data that you need less often. 

S3-IA is great for use cases such as backups and disaster recovery.

### Glacier

Glacier is the least expensive storage option in S3 but is designed for archival storage. You cannot fetch data from Glacier as fast as Standard or S3-IA, but it is a great option for long term data archival.

In addition to choosing one of these three storage classes, you can also set lifecycle policies in S3. This means that you can schedule files to be moved automatically to S3-IA or Glacier after a certain period of time.

## Why Use S3?

Companies like Netflix, Dropbox, and Reddit are avid users of S3. The popular file storage system Dropbox built its entire storage capacity on top of Amazon S3. 

Let’s look at some of the core features of S3 and understand why it's so popular among enterprises and startups alike.

### It's Affordable

S3 is cheap. I mean super cheap compared to other storage solutions. And with S3, you only pay for what you use. There are no upfront costs, no setup. It's just plug and play.

In addition to affordable pricing, S3 offers a Free tier. This free tier comes with 5GB of storage space, 20,000 GET Requests, 2,000 PUT, COPY, POST, or LIST Requests and 15GB of Data Transfer. The free tier is available every month for the first year.

With S3 you can avoid paying for space or bandwidth you might not even need.

### It's Scalable

S3 scales with your application. Since you pay only for that you use, there is no limit to the data you can store in S3.

This is helpful during multiple scenarios, especially during an unexpected surge in user growth. You don’t have to buy extra space. S3 has you covered.

### It's Secure

One of the many reasons companies prefer S3 is its inclination towards security. While you have to secure custom server setups, S3 is secure by default.

This does not mean you cannot store publicly accessible information in S3. S3 locks up all your data with high security unless you explicitly configure not to.

S3 also maintains compliance programs, such as PCI-DSS, HIPAA/HITECH, FedRAMP, EU Data Protection Directive, and FISMA, to help you meet your industry’s regulatory requirements.

### It Has Versioning

Versioning means keeping multiple copies of a file and tracking its changes over time. This is useful, especially when you handle sensitive data.

You can also retrieve accidentally deleted files when you enable versioning with S3.

However, if you enable versioning, you are storing multiple copies of the same document. This can have an effect on pricing as well as read/write requests you make. 

So just take that into account while integrating versioning for your application.

Versioning is disabled by default for S3 but you can enable versioning using the AWS Console.

### It's Durable

Data durability is an underrated feature of S3. Given how common data loss is among companies, data durability is a core factor to consider when building enterprise software.

S3 provides a highly durable storage infrastructure. S3 redundantly stores data in multiple facilities, making you data safe in the event of a system failure. S3 also performs regular data integrity checks to make sure your data is intact.

S3 offers 99.999999999% durability (called the 9s durability) and 99.99% availability of objects over a given year.

## S3 Use Cases

### Static Website Hosting

You can use S3 as a static website hosting platform. The difference between static and dynamic websites is that dynamic websites receive and process user input. Static websites are used only for displaying information.

With the advent of [Single Page Applications](https://en.wikipedia.org/wiki/Single-page_application), you can host a complete web app on S3, often free of charge. 

Frameworks like React and Angular have made user input processing happen within the browser. You can build a SPA that listens to third party APIs and host it within S3. 

S3 also has great support for routing, so you can use your own custom domain as well.

I recently wrote an article on hosting a React web app using S3 and [you can find the article here](https://medium.com/@manishmshiva/aws-s3-hosting-a-react-web-app-on-aws-s3-2ff2e8ca78dd).

### Analytics

You can run queries on your S3 data without moving your data to an analytics platform. This makes S3 a great use case for building powerful analytics applications.

S3 offers multiple options including S3 Select, Amazon Athena, and Amazon Redshift Spectrum. You can also combine these with [AWS Lambda](https://aws.amazon.com/lambda/) to perform data processing on the fly.

### File Sharing

Amazon S3 can be also used as a cheap file sharing solution. Like I mentioned earlier in the article, the famous file sharing service Dropbox was first built on top of S3.

With flexible security policies, you can configure your S3 buckets with custom permissions for different customers. S3 also offers [transfer acceleration](https://aws.amazon.com/s3/transfer-acceleration/#:~:text=S3%20Transfer%20Acceleration%20%28S3TA%29%20reduces,to%20S3%20for%20remote%20applications.) to speed up large file transfers across longer distances.

## Summary

Amazon S3 is a great tool to work with for your web or mobile application storage requirements. With on-demand pricing and scalability at its core, S3 has been the favored cloud storage solution for small and large businesses alike.

Companies from Netflix to Pinterest trust S3 with their data, thanks to the 99.999999999% data durability promise from Amazon. 

You can also use Amazon S3 as a personal storage solution or host your next project via static site hosting. In a nutshell, S3 is a great multi-purpose storage solution catering to a wide range of use cases.

_I regularly write about Machine Learning, Cyber Security, and AWS. You can signup for my_ [_weekly newsletter_](https://www.manishmshiva.com/) _here._

