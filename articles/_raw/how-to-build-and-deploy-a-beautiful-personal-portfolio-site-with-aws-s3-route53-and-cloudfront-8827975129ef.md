---
title: How to build and deploy a beautiful personal portfolio site with AWS S3, Route53,
  and CloudFront ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-10T21:03:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-and-deploy-a-beautiful-personal-portfolio-site-with-aws-s3-route53-and-cloudfront-8827975129ef
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lkRw8tZ_QI_tDfz0Tagufg.jpeg
tags:
- name: AWS
  slug: aws
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Nicholas Vincent-Hill

  This is a step-by-step guide to creating a responsive static billboard/portfolio
  site, deploying it to the web with AWS, and serving it securely with HTTPS.

  This guide is designed for beginner and intermediate-level software ...'
---

By Nicholas Vincent-Hill

_This is a step-by-step guide to creating a responsive static billboard/portfolio site, deploying it to the web with AWS, and serving it securely with HTTPS._

This guide is designed for beginner and intermediate-level software engineers and web developers looking for an easy way to create a personal site for cheaper than paid-services like SquareSpace or other site-builders. Basic technical requirements include a knowledge of HTML/CSS/JS, npm, and Git (the advanced site creation process uses Gatsby.js which requires knowledge of React.js and GraphQL).

The only economic requirements are AWS Route53 hosted zone fees ($0.50/month) and the cost of acquiring a domain (I rented nickvh.tech for $25 for five years from get.tech). Netlify is a free option as well. The estimated time commitment is four to five hours depending on individual skill and experience.

This guide will enable you, the developer, to control all aspects of the design, development, and deployment of your site.

#### **Step 1 — Create your personal site (the easy way or the hard way)**

**Here’s the easy way:** go [here](https://html5up.net/) and pick out a fully responsive, super customizable, and 100% free (under the [Creative Commons](https://html5up.net/license)) HTML/CSS/JS template. Download it and customize/build on it until you love it!

Create a `package.json` by calling `npm init` in the root directory of your chosen project. Make sure to `git init`, add all non-public information to `.gitignore`, and write great commit messages.

**Here’s the hard way:** use Gatsby.js to build a blazing fast static site and PWA from scratch. This isn’t a Gatsby.js tutorial (plenty of great tutorials can be found [here](https://www.gatsbyjs.org/tutorial/)) and requires React.js and GraphQL knowledge. A number of starter templates can be found [here](https://www.gatsbyjs.org/starters/?v=2) (I used the “strata” HTML5UP template as a jumping off point for [nickvh.tech](https://www.nickvh.tech/)).

Test and develop your website until you are happy with it and want to share it with the world. We will be building a continuous development pipeline with either Grunt or the `gatsby-plugin-s3` plugin later so future revisions/deployment will be quick and easy.

#### **Step 2 — Get a domain**

Sites like [https://get.tech](https://get.tech/) or [https://www.namecheap.com](https://www.namecheap.com/) offer very compelling prices for domains. I waited for a promotion and got [https://nickvh.tech](https://get.tech/) for $25 for five years. Alternatively buy a .dev domain from [Google](https://domains.google/#/).

#### **Step 3 — Create an AWS account**

Create an [AWS account](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/). This step is fairly straightforward. New accounts get free services for a year — outlined [here](https://aws.amazon.com/free/). This requires you to have an active credit card on file with AWS. **Be aware of the security implications and do not accidentally push your AWS credentials to the public web.**

#### **Step 4 — Configure AWS S3 buckets**

> _Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance. This means customers can use it to store and protect any amount of data for a range of use cases, such as websites, mobile applications, backup and restore, archive, enterprise applications, IoT devices, and big data analytics._

AWS S3 is where your static site will live; there are a few things to do in order to configure this correctly.

First create a bucket; AWS S3 and Route53 only work correctly if your bucket name and domain name match precisely — name your bucket mysite.domain (i.e. nickvh.tech). Make sure to set permissions correctly; the public should be able to read from the bucket but not write to it.

![Image](https://cdn-media-1.freecodecamp.org/images/1*nDKOVzwkcQamFyaTVWYDHw.png)
_Make sure to give public read access to your bucket_

Next navigate to “Properties” and configure AWS S3 to statically serve `index.html` (see below).

![Image](https://cdn-media-1.freecodecamp.org/images/1*jU6929oqVXSINz3o9LHJZg.png)

Create a bucket (also public read access enabled) named www.mysite.domain ([www.nickvh.tech](http://www.nickvh.tech) in my case) and redirect to the main bucket address (see below).

![Image](https://cdn-media-1.freecodecamp.org/images/1*3r7p-HOEkXp97fOOdA58dA.png)

Next, create `aws-keys.json` in the root directory of your project:

Here’s a [guide](https://help.bittitan.com/hc/en-us/articles/115008255268-How-do-I-find-my-AWS-Access-Key-and-Secret-Access-Key-) to finding your AWS access key ID and Secret key.

**Remember to add** `aws-keys.json` **to your** `.gitignore`**! One of my students accidentally pushed their AWS credentials to Github, was programmatically attacked, and incurred ~$1.3k in charges in a few hours.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*Vb3KlOUa_yZJ_yyZEz9zEg.png)
_Don’t let this happen to you!_

#### Step 5— Upload your site to AWS S3 with Grunt or `gatsby-plugin-s3`

> _Grunt is a JavaScript task runner, a tool used to automatically perform frequent tasks such as minification, compilation, unit testing, and linting. It uses a command-line interface to run custom tasks defined in a file._

If you choose the easy way to create your site, you can use Grunt to upload your completed site files to your AWS S3 bucket.

```
npm install grunt grunt-aws-s3 --save-dev
```

Create a `Gruntfile.js`:

Add this to the scripts object of your `package.json`.

```
"deploy": "grunt deploy"
```

Now whenever you want to deploy a new production version of your site just execute `npm run deploy`. This will only POST/PUT files to AWS S3 that have changed — reducing the number of requests you need to pay for (new AWS accounts get 2,000 free PUT requests/month for the first year).

Alternatively — if you built your site with Gatsby.js, forget Grunt and just use `gatsby-plugin-s3` for static site deployment. I wrote a npm script `npm run ship` which builds the production bundle and uploads it to AWS S3 - `gatsby build && gatsby-plugin-s3 deploy`. The code for my Gatsby site can be found [here](https://github.com/nvincenthill/portfolio_v3).

#### **Step 6— Create a distribution with AWS CloudFront**

> _Amazon CloudFront is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency, high transfer speeds, all within a developer-friendly environment._

Create a new CloudFront distribution (loosely following these [AWS docs](https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-https-requests-s3/)). Make sure to specify **Alternate Domain Names** **(CNAMEs)** correctly and request a custom SSL certificate to enable HTTPS.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dKBOI5qkk-JZUoTs4KOrHQ.png)

Also specify the **Default Root Object** as `index.html`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*YdRYM7Ygu_pHCViM6ARgYA.png)
_Remember to specify Default Root Object_

Click Create Origin to link your S3 bucket to your CloudFront Distribution. Specify **Origin Domain Name** as `YOUR_S3_BUCKET_NAME.s3.amazonaws.com`. Do not restrict bucket access.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Q2B1TcFuw2o9vvkXOXwnjQ.png)
_CloudFront Distribution Origin_

Create a new behavior and set **Viewer Protocol Policy** to “Redirect HTTP to HTTPS.”

![Image](https://cdn-media-1.freecodecamp.org/images/1*y7BAWIzgm-TCa_jdCBTKqA.png)
_CloudFront Distribution Behaviors_

You can also customize error responses — I redirect 404 errors to a custom 404.html page.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CyDZcVNq6o3FtA1fDGOjDw.png)
_CloudFront Error Pages_

#### **Step 7— Redirect traffic to your new CDN with AWS Route53**

> _Amazon Route 53 is a highly available and scalable cloud [Domain Name System (DNS)](https://aws.amazon.com/route53/what-is-dns/) web service. It is designed to give developers and businesses an extremely reliable and cost effective way to route end users to Internet applications by translating names like [www.example.com](http://www.example.com) into the numeric IP addresses like 192.0.2.1 that computers use to connect to each other._

Now we need to connect your domain name (mysite.domain) to your CloudFront distribution so that when a user makes a request to your domain they receive your `index.html` and the rest of your static site (by hitting your newly created CDN).

Open the AWS Route53 console and create a new **Hosted Zone**. Here’s some helpful [AWS docs](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/migrate-dns-domain-inactive.html) to get you started.

**Make sure to update the name servers for the domain you bought. Use the method provided by the registrar for the domain you purchased to change the name servers for the domain (use the four Route53 name servers found in the NS — Name server record set).**

Create a new record set and set the alias target to your AWS CloudFront distribution (see below). Make sure to name it yoursite.domain.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gDQ-77A2FQ0n3Qlr47vcaQ.png)
_Alias your CloudFront distribution_

Changes to domain name servers take time to propagate so make sure to wait a few minutes before attempting to access your site via your new domain.

#### Step 8— Bask in the glory of your newly deployed site! (or troubleshoot problems)

You did it! Enjoy your beautiful new portfolio site deployed to the world wide web. Check out [my site](http://nickvh.tech) I built and deployed using this tech stack; I wired up the contact form with AWS Lambda using [this guide](https://dev.to/adnanrahic/building-a-serverless-contact-form-with-aws-lambda-and-aws-ses-4jm0).

![Image](https://cdn-media-1.freecodecamp.org/images/1*lkRw8tZ_QI_tDfz0Tagufg.jpeg)
_Enjoy your new beautiful portfolio site! [html5up.com](http://html5up.com" rel="noopener" target="_blank" title=")_

> _Read Next:_

> [Scrabblr — A React game with react-dnd and react-flip-move](https://hackernoon.com/scrabblr-a-react-game-with-react-dnd-and-react-flip-move-40cfaac786e2)

