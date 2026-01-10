---
title: How to auto-create CloudWatch Alarms for APIs with CloudWatch Events and Lambda
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-13T17:57:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-auto-create-cloudwatch-alarms-for-apis-with-cloudwatch-events-and-lambda-b128920857aa
coverImage: https://cdn-media-1.freecodecamp.org/images/0*2Xre5dsJRMQqIrZA.png
tags:
- name: automation
  slug: automation
- name: AWS
  slug: aws
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Yan Cui

  In a pre­vi­ous post, I dis­cussed how to auto-sub­scribe a Cloud­Watch Log Group
  to a Lamb­da func­tion using Cloud­Watch Events. The benefit of this is that we
  don’t need a man­u­al process to ensure all Lamb­da logs are forwarded to our...'
---

By Yan Cui

In a [pre­vi­ous post](https://theburningmonk.com/2017/08/centralised-logging-for-aws-lambda/), I dis­cussed how to auto-sub­scribe a **Cloud­Watch Log Group** to a Lamb­da func­tion using **Cloud­Watch Events**. The benefit of this is that we don’t need a man­u­al process to ensure all Lamb­da logs are forwarded to our log aggre­ga­tion ser­vice.

![Image](https://cdn-media-1.freecodecamp.org/images/0*TVbE2siAsoz5JPxp.png)

Whilst this is use­ful in its own right, it only scratch­es the sur­face of what we can do. **Cloud­Trail** and **Cloud­Watch Events** make it easy to auto­mate many day-to-day oper­a­tional steps, with the help of **Lamb­da** of course ?

![Image](https://cdn-media-1.freecodecamp.org/images/0*2Xre5dsJRMQqIrZA.png)

I work with **API Gate­way** and **Lamb­da** a lot. When­ev­er you cre­ate a new API, or make changes, there are sev­er­al things you need to do:

* Enable **Detailed Met­rics** for the deploy­ment stage
* Set up a dash­board in Cloud­Watch, show­ing request count, laten­cies, and error counts
* Set up **Cloud­Watch Alarms** for P99 laten­cies and error counts

Because these are man­u­al steps, they often get missed.

Have you ever for­got­ten to update the dash­board after adding a new end­point to your API? And did you also remem­ber to set up a P99 laten­cy alarm on this new end­point? How about alarms on the number of 4XX or 5xx errors?

Most teams I’ve dealt with have some con­ven­tions around these, but they don’t have a way to enforce them. The result is that the con­ven­tion is applied in patch­es and can­not be relied upon. I find that this approach doesn’t scale with the size of the team.

It works when you’re a small team. Every­one has a shared under­stand­ing, and the nec­es­sary dis­ci­pline to fol­low the con­ven­tion. When the team gets big­ger, you need automa­tion to help enforce these con­ven­tions.

For­tu­nate­ly, we can auto­mate away these man­u­al steps using the same pattern. In the [Mon­i­tor­ing](https://livevideo.manning.com/module/38_9_5/) unit of my course [Pro­duc­tion-Ready Server­less](https://bit.ly/production-ready-serverless), I demon­strat­ed how you can do this in 3 sim­ple steps:

* **Cloud­Trail** cap­tures the **Cre­at­eDe­ploy­ment** request to **API Gate­way**
* **Cloud­Watch Events** pat­tern against this cap­tured request
* **Lamb­da** func­tion to enable detailed met­rics, and cre­ate alarms for each end­point

If you use the [Server­less](https://serverless.com/framework/docs/) frame­work, then you might have a func­tion that looks like this:

A cou­ple of things to note from the code above:

* I’m using the [server­less-iam-roles-per-func­tion](https://github.com/functionalone/serverless-iam-roles-per-function) plu­g­in to give the func­tion a tai­lored IAM role
* The func­tion needs the `apigateway:PATCH` per­mis­sion to enable detailed met­rics
* The func­tion needs the `apigateway:GET` per­mis­sion to get the API name and REST end­points
* The func­tion needs the `cloudwatch:PutMetricAlarm` per­mis­sion to cre­ate the alarms
* The envi­ron­ment vari­ables spec­i­fy SNS top­ics for the **Cloud­Watch Alarms**

The cap­tured event looks like this:

We can find the `restApiId` and `stageName` inside the `detail.requestParameters` attribute. That’s all we need to fig­ure out what end­points are there, and so what alarms we need to cre­ate.

Inside the han­dler func­tion, which you can find [here](https://github.com/theburningmonk/manning-aws-lambda-in-motion/blob/master/functions/create-alarms.js), we per­form a few steps:

* Enable detailed met­rics with an `updateStage` call to API Gate­way
* Get the list of REST end­points with a `getResources` call to API Gate­way
* Get the REST API name with a `getRestApi` call to API Gate­way
* For each of the REST end­points, cre­ate a P99 laten­cy alarm in the `AWS/ApiGateway` name­space

![Image](https://cdn-media-1.freecodecamp.org/images/0*4jj_jV1dNe8XMyEE.png)

Now, every time I cre­ate a new API, I will have **Cloud­Watch Alarms** to alert me when the 99 per­centile laten­cy for an end­point goes over 1 sec­ond, for 5 minutes in a row.

All this, with just a few lines of code ?

![Image](https://cdn-media-1.freecodecamp.org/images/0*rXmrxT-GCnEEprlK.png)

You can take this fur­ther, and have oth­er Lamb­da func­tions to:

* Cre­ate Cloud­Watch Alarms for 5xx errors for each end­point
* Cre­ate Cloud­Watch Dash­board for the API

So there you have it! A use­ful pat­tern for automat­ing away man­u­al operational tasks.

And before you tell me about the [ACloudGuru AWS Alerts Serverless plugin](https://github.com/ACloudGuru/serverless-plugin-aws-alerts) by the ACloudGuru folks, yes I’m aware of it. It looks neat, but it’s ulti­mate­ly still some­thing the developer has to remem­ber to do.

That requires dis­ci­pline.

My expe­ri­ence tells me that you can­not rely on dis­ci­pline, ever. Which is why I pre­fer to have a plat­form in place that will gen­er­ate these alarms instead.

