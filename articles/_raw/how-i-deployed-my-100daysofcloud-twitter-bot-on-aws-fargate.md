---
title: 'How I Deployed My #100DaysOfCloud Twitter Bot on AWS Fargate'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-13T02:31:55.000Z'
originalURL: https://freecodecamp.org/news/how-i-deployed-my-100daysofcloud-twitter-bot-on-aws-fargate
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c99c3740569d1a4ca2191.jpg
tags:
- name: 100DaysOfCloud
  slug: 100daysofcloud
- name: AWS
  slug: aws
- name: Devops
  slug: devops
- name: Docker
  slug: docker
seo_title: null
seo_desc: 'By Johan Rin

  After passing my last certification, I asked myself how much time I spent studying
  cloud computing.

  https://twitter.com/johanrin/status/1276049320748425216

  More than 100 days!

  It also made me realize two things:


  There was no #100DaysOfC...'
---

By Johan Rin

After passing my last certification, I asked myself how much time I spent studying cloud computing.

%[https://twitter.com/johanrin/status/1276049320748425216]

More than 100 days!

It also made me realize two things:

1. There was no #100DaysOfCloud challenge
2. We have now enough content to create this challenge

So I immediately contacted Alex Kallaway, the creator of #100DaysOfCode, to ask him if it was possible to create #100DaysOfCloud based on his challenge.

And a few days later, the #100DaysOfCloud challenge was official:

%[https://twitter.com/johanrin/status/1276409322596155616]

But something was missing.

If you already used the #100DaysOfCode hashtag, you know that your tweets are going to be retweeted at least three times by Twitter bots.

Because there were no bots for the new #100DaysOfCloud challenge, I decided to fix that problem.

In this post, we're gonna see how I deployed my Twitter bot and why I choose to deploy it on AWS Fargate.

Let's start!

## Prerequisites

If you want to follow along and run the commands below, be sure to:

* Have an [AWS account with access key and secret key](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys)
* Have [Twitter API Authentication Credentials](https://developer.twitter.com/)
* Install [Docker](https://docs.docker.com/get-docker/) on your machine
* Clone the repository from [https://github.com/johanrin/100-days-of-cloud-bot](https://github.com/johanrin/100-days-of-cloud-bot)

## Why AWS Fargate?

If you check my code, you’ll see that:

* The code is written in Python and use tweepy package
* The bot is always running (using a `while` loop)
* There is a `Dockerfile` to build my image

I will not explain all the code because that's beyond the scope of this post. But I did mention all the sources I used in the GitHub repository.

My idea was to deploy the Docker image in a container in the cloud with the following constraints:

1. I don't want to spend much money
2. I don't want to manage and operate servers

Because I have credits on AWS, the first constraint was easy — go with AWS.

As for constraint number 2, I knew from the [AWS Certified Developer - Associate course](https://youtu.be/RrKRN9zRBWs), that we could deploy serverless containers with AWS Fargate.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Screenshot_2020-07-08-AWS-Certified-Developer---Associate-2020--PASS-THE-EXAM---Ad-Free-Course.png)
_From the AWS Certified Developer - Associate 2020 course_

Depending on your region, the pricing for AWS services can vary. It's often just a matter of a few cents, but I planned to run my bot for at least one year. So, every cent mattered.

To see AWS Fargate pricing and minimize your cost, you can [check the AWS documentation](https://aws.amazon.com/fargate/pricing/). I found that the cheapest region close to me was Ireland, so I decided to deploy my bot to AWS Fargate there.

## How did I deploy my bot?

Now that I've explained why I used AWS Fargate, let's see how I deployed my bot.

There are two big steps to deploy a Docker image on AWS Fargate:

1. Push the Docker image to Amazon Elastic Container Registry (ECR)
2. Deploy the Docker image on Fargate

Let's explain each step in detail.

### Push the Docker image to Amazon Elastic Container Registry (ECR)

* In the root directory, build your image from the `Dockerfile`.

```bash
docker build . -t 100-days-of-cloud-bot
```

* Authenticate your Docker to Amazon ECR.

```bash
aws ecr get-login-password --region region | docker login --username AWS --password-stdin aws_account_id.dkr.ecr.region.amazonaws.com
```

* Tag your image with the Amazon ECR repository.

```bash
docker tag 100-days-of-cloud-bot aws_account_id.dkr.ecr.region.amazonaws.com/100-days-of-cloud-bot
```

* Push your image to Amazon ECR.

```bash
docker push aws_account_id.dkr.ecr.region.amazonaws.com/100-days-of-cloud-bot
```

### Deploy the Docker image on Amazon Fargate

* Open the [Amazon ECS console first run wizard](https://console.aws.amazon.com/ecs/home#/firstRun).

![Image](https://www.freecodecamp.org/news/content/images/2020/07/01-Screenshot_2020-06-30-Amazon-ECS.png)

* Click **Configure** in the custom container, complete with the following settings, and then select **Update**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Image1.png)

| Property                                                                | Value                                                                                                                                                                              |
| ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Container name**                                                      | container-100-days-of-cloud-bot                                                                                                                                                    |
| **Image**                                                               | aws_account_id.dkr.ecr.region.amazonaws.com/100-days-of-cloud-bot                                                                                                                  |
| **Memory Limits (MiB)**                                                 | Soft Soft limit \| 512                                                                                                                                                                   |
| **Port mappings**                                                       | _Container port_: 80<br />_Protocol_: tcp                                                                                                                                          |
| **CPU units**                                                           | 256                                                                                                                                                                                |
| **Environment variables**<br />(Twitter API Authentication Credentials) | CONSUMER_KEY \| Value \| consumer_key<br />CONSUMER_SECRET \| Value \| consumer_secret<br />ACCESS_TOKEN \| Value \| access_token<br />ACCESS_TOKEN_SECRET \| Value \| access_token_secret |


* Click **Edit** in the **Task definition** section, complete with the following settings, and then select **Save**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Image1-1.png)

| Property                 | Value                                 |
| ------------------------ | ------------------------------------- |
| **Task definition name** | task-definition-100-days-of-cloud-bot |
| **Task memory**          | 0.5GB (512)                           |
| **Task CPU**             | 0.25 vCPU (256)                       |


* Click **Next**.
* Click **Edit** in the **Define your service** section, complete with the following settings, and then select **Save**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Image2.png)

| Property                    | Value                         |
| --------------------------- | ----------------------------- |
| **Service name**            | service-100-days-of-cloud-bot |
| **Number of desired tasks** | 1                             |
| **Load balancer type**      | None                          |

We don't need a load balancer here because of the Twitter API rate limit. Even if we scale-out our containers, Twitter's API will send us a 420 error message because the bot is being rate limited for making too many requests.

* Click **Next**.
* Edit your **Cluster name** with cluster-100-days-of-cloud-bot.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/12-Screenshot_2020-06-30-Amazon-ECS.png)

* Click **Next**.
* Review your configuration and click **Create**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/16-Screenshot_2020-06-30-Amazon-ECS.png)

That's it, the container is deployed on AWS Fargate!

## Conclusion

You deployed your Twitter bot on AWS Fargate with only four steps.  

AWS Fargate is easy to use, allowing us to deploy containers without managing and operating servers.

This use case was simple, but we can do much more like adding a load balancer or defining more tasks. I recommend you to [check the documentation](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html) for more details.

Because this post was about the #100DaysOfCloud challenge, I should mention that we have [Discord server](https://discord.com/invite/c6Db8nY), so feel free to join the community and the challenge! We have amazing people from all around the world ready to help you to get started with the Cloud.

That's it for me, hope you learned something! If you have any questions, [find me on Twitter](https://twitter.com/johanrin) and feel free to ask me anything. 

