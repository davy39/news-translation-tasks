---
title: How to implement log aggregation for AWS Lambda
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-31T09:00:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-implement-log-aggregation-for-aws-lambda-ca714bf02f48
coverImage: https://cdn-media-1.freecodecamp.org/images/1*gV8PnF93tCU_3wmWxBxn4A.png
tags:
- name: AWS
  slug: aws
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: UX
  slug: ux
seo_title: null
seo_desc: 'By Yan Cui

  Dur­ing the exe­cu­tion of a Lamb­da func­tion, what­ev­er you write to std­out
  (for example, using console.log in Node.js) will be cap­tured by Lamb­da and sent
  to Cloud­Watch Logs asyn­chro­nous­ly in the back­ground. And it does this wi...'
---

By Yan Cui

Dur­ing the exe­cu­tion of a Lamb­da func­tion, what­ev­er you write to std­out (for example, using `console.log` in Node.js) will be cap­tured by Lamb­da and sent to Cloud­Watch Logs asyn­chro­nous­ly in the back­ground. And it does this with­out adding any over­head to your func­tion exe­cu­tion time.

You can find all the logs for your Lamb­da func­tions in Cloud­Watch Logs. There is a unique log group for each func­tion. Each log group then consists of many log streams, one for each concurrently executing instance of the function.

![Image](https://cdn-media-1.freecodecamp.org/images/kjX-pl1TyZV2Pd45dYwGv2NlJoEQCBL5ygIc)

You can send logs to Cloud­Watch Logs your­self via the [Put­Lo­gEvents](http://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.html) oper­a­tion. Or you can send them to your pre­ferred log aggre­ga­tion ser­vice such as Splunk or Elas­tic­search.

But, remem­ber that **every­thing has to be done dur­ing a function’s invocation**. If you make addi­tion­al net­work calls dur­ing the invo­ca­tion, then you’ll pay for that addi­tion­al exe­cu­tion time. Your users would also have to wait longer for the API to respond.

These extra network calls might only add 10–20ms per invocation. But you have microservices, and a single user action can involve several API calls. Those 10–20ms per API call can compound and add over 100ms to your user-facing latency, which is enough to [reduce sales by 1% according to Amazon](https://blog.gigaspaces.com/amazon-found-every-100ms-of-latency-cost-them-1-in-sales/).

So, don’t do that!

Instead, process the logs from Cloud­Watch Logs after the fact.

In the Cloud­Watch Logs con­sole, you can select a log group and choose to stream the data direct­ly to Amazon’s host­ed Elas­tic­search ser­vice.

![Image](https://cdn-media-1.freecodecamp.org/images/D6vXlFNTuMjMQcM9h19AyK2lgEMeVHAi6y-Z)

This is very use­ful if you’re using the host­ed Elas­tic­search ser­vice already. But if you’re still eval­u­at­ing your options, then give [this post](https://read.acloud.guru/things-you-should-know-before-using-awss-elasticsearch-service-7cd70c9afb4f) a read before you decide on the AWS-host­ed Elas­tic­search.

You can also stream the logs to a Lamb­da func­tion instead. There are even a num­ber of Lambda function blue­prints for push­ing Cloud­Watch Logs to oth­er log aggre­ga­tion ser­vices already.

Clear­ly this is some­thing a lot of AWS’s cus­tomers have asked for.

![Image](https://cdn-media-1.freecodecamp.org/images/UY-1KkwDlx2RcjeGTyzncQ9cCZknZGvsaMNd)
_You can find blue­prints for ship­ping Cloud­Watch Logs to Sumo­log­ic, Splunk and Log­gly out of the box._

You can use these blue­prints to help you write a Lamb­da func­tion that’ll ship Cloud­Watch Logs to your pre­ferred log aggre­ga­tion ser­vice. But here are a few more things to keep in mind.

When­ev­er you cre­ate a new Lamb­da func­tion, it’ll cre­ate a new log group in Cloud­Watch logs. You want to avoid a man­u­al process for sub­scrib­ing log groups to your log shipping func­tion.

Instead, enable Cloud­Trail, and then set­up an event pat­tern in Cloud­Watch Events to invoke anoth­er Lamb­da func­tion when­ev­er a log group is cre­at­ed.

You can do this one-off set­up in the Cloud­Watch con­sole.

![Image](https://cdn-media-1.freecodecamp.org/images/031B7URKw4Nxa9j7hdWfWNv9odyBFe4UmPXF)
_Match the Cre­ateL­og­Group API call in Cloud­Watch Logs and trig­ger a sub­scribe-log-group Lamb­da func­tion. This function would sub­scribe the new log group to the log shipping func­tion._

If you’re work­ing with mul­ti­ple AWS accounts, then you should avoid mak­ing the set­up a man­u­al process. With the [Server­less](https://serverless.com/framework/) frame­work, you can set­up the event source for this `subscribe-log-group` func­tion in the `serverless.yml`.

![Image](https://cdn-media-1.freecodecamp.org/images/DHuTPlIAXa-X614O4KinqB80M74H5I5KDgI3)

Anoth­er thing to keep in mind is that **you need to avoid sub­scrib­ing the log group for the** `ship-logs` **func­tion to itself.** It’ll cre­ate **an infi­nite invo­ca­tion loop** and that’s a _painful_ les­son that you want to avoid.

One more thing.

By default, when Lamb­da cre­ates a new log group for your func­tion, the retention pol­i­cy is set to `Never Expire`. This is overkill, as the [data storage cost](https://aws.amazon.com/cloudwatch/pricing/) can add up over time. It’s also unnecessary if you’re shipping the logs elsewhere already!

![Image](https://cdn-media-1.freecodecamp.org/images/nzZDmkdrPAmbAh8z7QFDHd-XUxtnQFzGdsTT)
_By default, logs for your Lamb­da func­tions are kept in CloudWatch Logs for­ev­er_

We can apply the same tech­nique above and add anoth­er Lamb­da func­tion to automatically update the reten­tion pol­i­cy to some­thing more rea­son­able.

![Image](https://cdn-media-1.freecodecamp.org/images/gvD8ZPfcTRQq4TeV4RW1gE0S0momJHWHDEGO)
_Here’s a Lamb­da func­tion for auto-updat­ing the log reten­tion pol­i­cy to 30 days._

If you already have lots of exist­ing log groups, then con­sid­er writing one-off [scripts](https://github.com/theburningmonk/lambda-logging-demo/blob/master/process_all.js) to update them all. You can do this by [recurs­ing](https://github.com/theburningmonk/lambda-logging-demo/blob/master/process_all.js#L21-L35) through all log groups with the [DescribeL­og­Groups](http://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeLogGroups.html) API call.

If you’re interested in applying these techniques yourself, I have put together a simple [demo project](https://github.com/theburningmonk/lambda-logging-demo) for you. If you follow the instructions in the README and deploy the functions, then all the logs for your Lambda functions would be delivered to [Logz.io](https://logz.io/).

