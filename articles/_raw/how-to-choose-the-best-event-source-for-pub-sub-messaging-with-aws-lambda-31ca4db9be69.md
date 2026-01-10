---
title: How to choose the best event source for pub/sub messaging with AWS Lambda
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-02T21:38:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-choose-the-best-event-source-for-pub-sub-messaging-with-aws-lambda-31ca4db9be69
coverImage: https://cdn-media-1.freecodecamp.org/images/0*dEUcN2mmJXDmiwb8.png
tags:
- name: AWS
  slug: aws
- name: messaging
  slug: messaging
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: null
seo_desc: 'By Yan Cui

  AWS offers a wealth of options for imple­ment­ing mes­sag­ing pat­terns such as
  Publish/Subscribe (often short­ened to pub/sub) with AWS Lamb­da. In this article,
  we’ll com­pare and con­trast some of these options.

  The pub/sub pattern

  Pub/...'
---

By Yan Cui

AWS offers a wealth of options for imple­ment­ing mes­sag­ing pat­terns such as `Publish/Subscribe` (often short­ened to pub/sub) with AWS Lamb­da. In this article, we’ll com­pare and con­trast some of these options.

### The pub/sub pattern

Pub/Sub is a mes­sag­ing pat­tern where pub­lish­ers and sub­scribers are decou­pled through an inter­me­di­ary message bro­ker (ZeroMQ, Rab­bit­MQ, SNS, and so on).

![Image](https://cdn-media-1.freecodecamp.org/images/aMYeJtlvg8qD1aw7GWlpLcrptCADpvXiGRlt)
_Source: [Publish Subscribe Pattern (Wikipedia)](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern" rel="noopener" target="_blank" title=")_

![Image](https://cdn-media-1.freecodecamp.org/images/in-2N2y0wjCxQdEAMjGcplRv7yUWRfMvewOr)

In the AWS ecosys­tem, the obvi­ous can­di­date for the bro­ker role is Simple Notification Service (SNS).

SNS will make three attempts for your Lambda func­tion to process a mes­sage before send­ing it to a Dead Let­ter Queue (DLQ) if a DLQ is spec­i­fied for the func­tion. How­ev­er, accord­ing to an [analy­sis](https://engineering.opsgenie.com/aws-lambda-performance-series-part-2-an-analysis-on-async-lambda-fail-retry-behaviour-and-dead-b84620af406) by the folks at Ops­Ge­nie, the number of retries can be as many as six.

Anoth­er thing to con­sid­er is the degree of par­al­lelism this set­up offers. For each mes­sage, SNS will cre­ate a new invo­ca­tion of your func­tion. So if you pub­lish 100 mes­sages to SNS, then you can have 100 con­cur­rent exe­cu­tions of the sub­scribed Lamb­da func­tion.

**This is great if you’re opti­mis­ing for through­put**.

![Image](https://cdn-media-1.freecodecamp.org/images/lKqW9l3keN4ybs4AHSxxJSu76E22YUADwgWE)

How­ev­er, we’re often **con­strained** by the max through­put our down­stream depen­den­cies can han­dle — data­bas­es, S3, internal/external ser­vices, and so on.

If the burst in through­put is short, then there’s a good chance the retries would be suf­fi­cient (there’s a ran­domized, expo­nen­tial back off between retries too) and you won’t miss any mes­sages.

![Image](https://cdn-media-1.freecodecamp.org/images/aUrhbLV0y5hatCjtR-kpZuvzi6eQZBmM9Gtz)
_Erred messages are retried 2 times with exponential back off. If the burst is short-lived then the retry is likely to succeed, resulting in no message loss._

If the burst in through­put is sus­tained over a long peri­od of time, then you can exhaust the max number of retries. At this point you’ll have to rely on the DLQ and pos­si­bly human inter­ven­tion in order to recov­er the mes­sages that couldn’t be processed the first time around.

![Image](https://cdn-media-1.freecodecamp.org/images/2uzNYBIHpLiAdHSsZBRl9aLIXXbKM5mQ5LBG)
_Erred messages are retried 2 times with exponential back off. But the burst in message rate overlaps with the retries, further exacerbating the problem and eventually the max number of retries are exhausted and erred messages have to be delivered to the DLQ instead (if one is specified)._

Sim­i­lar­ly, if the down­stream depen­den­cy expe­ri­ences an out­age, then all mes­sages received and retried dur­ing the out­age are bound to fail.

![Image](https://cdn-media-1.freecodecamp.org/images/PFbSpQtb0Nxx2RREF9VATvUBjJxR5lxu0WD5)
_Any message received or retried during the downstream message will fail and be sent to the DLQ._

You can also run into the [Lamb­da lim­it](http://docs.aws.amazon.com/lambda/latest/dg/limits.html) on the number of con­cur­rent exe­cu­tions in a region. Since this is an account-wide lim­it, it will also impact your oth­er sys­tems within the account that rely on AWS Lamb­da: APIs, event pro­cess­ing, cron jobs, and so on.

![Image](https://cdn-media-1.freecodecamp.org/images/MdSMzBdPAvsgSkw47bXD2Dj8qlB4K9y0v5fd)

SNS is also prone to suf­fer from tem­po­ral issues, like bursts in traf­fic, down­stream out­age, and so on. Kine­sis, on the oth­er hand, deals with these issues much bet­ter as described below:

* The degree of par­al­lelism is con­strained by the number of shards, which can be used to amor­tize bursts in the mes­sage rate

![Image](https://cdn-media-1.freecodecamp.org/images/MvIaF-A3FjeFNn5GSzSRzJ3vD-fcdF5kZv9q)
_Bursts in message rate is amortised, as the max throughput is determined by no. of shards * max batch size * 5 reads per second. Which gives you two levers to adjust the max throughput with._

* Records are retried until suc­cess is achieved, unless the out­age lasts longer than the reten­tion pol­i­cy you have on the stream (the default is 24 hours). You will even­tu­al­ly be able to process the records

![Image](https://cdn-media-1.freecodecamp.org/images/v8c03ATaEUayJurzgbxbPSWtqG-rebS7v40U)
_The impact of a downstream outage is absorbed by the retry-until-success invocation policy._

But Kine­sis Streams is not with­out its own prob­lems. In fact, from my expe­ri­ence using Kine­sis Streams with Lamb­da, I have found a number of caveats that need­ to be under­stood in order to make effec­tive use of the service.

You can read about these caveats in another article I wrote [here](https://read.acloud.guru/aws-lambda-3-pro-tips-for-working-with-kinesis-streams-8f6182a03113).

Inter­est­ing­ly, Kine­sis Streams is not the only stream­ing option avail­able on AWS. There is also DynamoDB Streams.

![Image](https://cdn-media-1.freecodecamp.org/images/ZVV6125FoRnsc-WWr5xDeiQdYMgdJgbxZFbn)
_DynamoDB Streams can be used as a like-for-like replacement for Kinesis Streams._

By and large, DynamoDB Streams + Lamb­da works the same way as Kine­sis Streams + Lamb­da. Oper­a­tional­ly, it does have some inter­est­ing twists:

* DynamoDB Streams auto scales the number of shards
* If you’re pro­cess­ing DynamoDB Streams with AWS Lamb­da, then you don’t pay for the reads from DynamoDB Streams (but you still pay for the read and write capac­i­ty units for the DynamoDB table itself)

![Image](https://cdn-media-1.freecodecamp.org/images/elMIs2s1bvzsS3t1s6lck8kKjUQtoN16p2d6)
_Source: [DynamoDB Pricing](https://aws.amazon.com/dynamodb/pricing/" rel="noopener" target="_blank" title=")_

* Kine­sis Streams offers the option to extend data reten­tion to 7 days, but DynamoDB Streams doesn’t offer such an option

![Image](https://cdn-media-1.freecodecamp.org/images/ZfHR49h8Odv-6oORBUdbEoulWBpkeTobaFSV)
_Source: [Working with DynamoDB Streams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html" rel="noopener" target="_blank" title=")_

The fact that DynamoDB Streams auto scales the number of shards can be a dou­ble-edged sword. On one hand, it elim­i­nates the need for you to man­age and scale the stream (or come up with home-baked [auto scal­ing solu­tions](https://read.acloud.guru/auto-scaling-kinesis-streams-with-aws-lambda-299f9a0512da)). But on the oth­er hand, it can also dimin­ish the abil­i­ty to amor­tize spikes in the load you pass on to down­stream sys­tems.

As far as I know, there is no way to lim­it the number of shards a DynamoDB stream can scale up to, which is some­thing you’d sure­ly con­sid­er when imple­ment­ing your own auto scal­ing solu­tion.

I think the most per­ti­nent ques­tion is, `“what is your source of truth?”`

Does a row being writ­ten in DynamoDB make it canon to the state of your system? This is cer­tain­ly the case in most N-tier sys­tems that are built around a data­base, regard­less of whether it’s an RDBMS or NoSQL database.

In an event-sourced sys­tem where state is mod­eled as a sequence of events (as opposed to a snap­shot), the source of truth might well be the Kine­sis stream. For example, as soon as an event is writ­ten to the stream, it’s con­sid­ered canon to the state of the sys­tem.

Then, there’re oth­er con­sid­er­a­tions around cost, auto-scal­ing, and so on.

From a devel­op­ment point of view, DynamoDB streams also have some limitations and short­com­ings:

* Each stream is lim­it­ed to events from one table
* The records describe DynamoDB events and not events from your domain, which I’ve always felt cre­ates a sense of dis­so­nance when work­ing with these events

Exclud­ing the cost of Lamb­da invo­ca­tions for pro­cess­ing the mes­sages, here are some cost pro­jec­tions for using SNS vs Kine­sis Streams vs DynamoDB Streams as the bro­ker. I’m mak­ing the assump­tion that through­put is con­sis­tent, and that each mes­sage is 1KB in size.

**Month­ly cost at 1 msg/s**

![Image](https://cdn-media-1.freecodecamp.org/images/yyuEQdQUtDXmaG-3FeSvBuM3Y1quo52SkIQY)

**Month­ly cost at 1,000 msg/s**

![Image](https://cdn-media-1.freecodecamp.org/images/11RcJ9KEIfnJbOCXvUz8g2J2AR6K5lKuGsNX)

**These pro­jec­tions should not be tak­en at face val­ue.** For starters, the assump­tion about a per­fect­ly con­sis­tent through­put and mes­sage size is unre­al­is­tic, and you’ll need some head­room with Kine­sis and DynamoDB streams even if you’re not hit­ting the throt­tling lim­its.

That said, what these pro­jec­tions do tell me is that:

1. You get an awful lot with each shard in Kine­sis streams
2. While there’s a base­line cost for using Kine­sis streams, the cost goes down when usage scales up as com­pared to SNS and DynamoDB streams, thanks to the sig­nif­i­cant­ly low­er cost per mil­lion requests

Whilst SNS, Kine­sis, and DynamoDB streams are your basic choic­es for the bro­ker, Lamb­da func­tions can also act as bro­kers in their own right and prop­a­gate events to oth­er ser­vices.

This is the approach used by the [aws-lamb­da-fanout](https://github.com/awslabs/aws-lambda-fanout) project from awslabs. It allows you to prop­a­gate events from Kine­sis and DynamoDB streams to oth­er ser­vices that can­not direct­ly sub­scribe to the three basic choice of bro­kers (either because of account/region lim­i­ta­tions or that they’re just not sup­port­ed).

![Image](https://cdn-media-1.freecodecamp.org/images/arPDE4lmFHJ-GPKb3u-366nUFaDeaZxiyZp8)
_The aws-lambda-fanout project from awslabs propagates events from Kinesis and DynamoDB Streams to other services across multiple accounts and regions._

While it’s a nice idea and def­i­nite­ly meets some spe­cif­ic needs, it’s worth bear­ing in mind the extra com­plex­i­ties it intro­duces, such as han­dling par­tial fail­ures, deal­ing with down­stream out­ages, mis­con­fig­u­ra­tions, and so on.

### Conclusion

So what is the best event source for doing pub-sub with AWS Lamb­da? Like most tech deci­sions, it depends on the **prob­lem** you’re try­ing to solve, and the **con­straints** you’re work­ing with.

In this post, we looked at SNS, Kine­sis Streams, and DynamoDB Streams as can­di­dates for the bro­ker role. We walked through a num­ber of sce­nar­ios to see how the choice of event source affects scal­a­bil­i­ty, par­al­lelism, and resilience against tem­po­ral issues and cost.

You should now have a much bet­ter under­stand­ing of the trade­offs between various event sources when work­ing with Lamb­da.

Until next time!

