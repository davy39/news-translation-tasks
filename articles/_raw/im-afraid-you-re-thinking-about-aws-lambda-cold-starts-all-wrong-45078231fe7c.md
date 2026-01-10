---
title: I’m afraid you’re thinking about AWS Lambda cold starts all wrong
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-17T09:30:29.000Z'
originalURL: https://freecodecamp.org/news/im-afraid-you-re-thinking-about-aws-lambda-cold-starts-all-wrong-45078231fe7c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JMd9a_VwVAA8pRSLChu3gQ.jpeg
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Yan Cui

  When I dis­cuss AWS Lamb­da cold starts with folks in the con­text of API Gate­way,
  I often get respons­es along the line of:


  Meh, it’s only the first request right? So what if one request is slow, the next
  mil­lion requests would be fast...'
---

By Yan Cui

When I dis­cuss AWS Lamb­da cold starts with folks in the con­text of API Gate­way, I often get respons­es along the line of:

> Meh, it’s only the first request right? So what if one request is slow, the next mil­lion requests would be fast.

Unfor­tu­nate­ly, that is an over­sim­pli­fi­ca­tion of what hap­pens.

Cold start hap­pens **once** for each **con­cur­rent exe­cu­tion** of your func­tion.

API Gate­way reuses con­cur­rent exe­cu­tions of your func­tion if pos­si­ble. Based on my obser­va­tions, it **_might_** _even queue up requests for a short time in the hope that one of the con­cur­rent exe­cu­tions would fin­ish and become reusable_.

If user requests hap­pen one after anoth­er, then you will only expe­ri­ence one cold start in the process. You can sim­u­late this using [Charles proxy](https://www.charlesproxy.com/) by repeating a cap­tur­ed request with a con­cur­ren­cy set­ting of 1.

![Image](https://cdn-media-1.freecodecamp.org/images/uh1CpqN69lXmbg8-5a5iiPdt7ylXQz37mQks)

As you can see in the time­line below, only the first request expe­ri­enced a cold start. The response for this request was much slow­er than the rest.

1 out of 100 — that’s bear­able. Hell, it won’t even show up in my 99 per­centile laten­cy met­ric.

![Image](https://cdn-media-1.freecodecamp.org/images/LXCAeq5zIW9SIMwX5onEKXBY7AKkYbT4GoYB)

What if the user requests came in droves instead? After all, user behav­iours are unpre­dictable and unlike­ly to fol­low the nice sequen­tial pat­tern we see above. So let’s sim­u­late what hap­pens when we receive 100 requests with a con­cur­ren­cy of 10.

![Image](https://cdn-media-1.freecodecamp.org/images/6HkV4EEduReCYILMg7mT8ISRBK-QmqZSjcdp)

![Image](https://cdn-media-1.freecodecamp.org/images/j7l6PzmEfzlKSfepxZttY8GvSImfaRfS17ix)

Now things don’t look quite as rosy — the first 10 requests were all cold starts! This is problematic if your traf­fic pat­tern is bursty around spe­cif­ic times of the day or spe­cif­ic events, for example:

* Food order­ing ser­vices (like JustEat and Deliv­eroo) have bursts of traf­fic around meal times
* e-com­mence sites have high­ly con­cen­trat­ed bursts of traf­fic around pop­u­lar shop­ping days of the year — like Cyber Mon­day and Black Fri­day
* Bet­ting ser­vices have bursts of traf­fic around sport­ing events
* Social net­works have bursts of traf­fic around notable events hap­pen­ing around the world

For these ser­vices, the sud­den bursts of traf­fic means API Gate­way would add more con­cur­rent exe­cu­tions of your Lamb­da func­tion. That equates to bursts of cold starts, and that’s bad news for you.

These are also the most cru­cial peri­ods for your busi­ness when you want your ser­vice to be on its best behav­ior.

![Image](https://cdn-media-1.freecodecamp.org/images/WCGWkW58PVn3dwqF9JEhWolUGoi9St-u8YuY)

If the spikes are predictable, then you can mitigate the effect of cold starts by pre-warming your API.

For example, in the case of a food ordering service, you know there will be a burst of traffic at noon. You can schedule a cron job using a CloudWatch scheduled event at 11:58am to trigger a Lambda function. This function would generate a burst of concurrent requests to force API Gateway to spawn the desired number of concurrent executions ahead of time.

You can use HTTP headers to tag these requests. The handling function can then distinguish them from normal user requests and short-circuit.

![Image](https://cdn-media-1.freecodecamp.org/images/11OPD33TBj4y9soH958GXVsYd4OhRNktSAjG)

**Does it not betray the ethos of serverless computing that you shouldn’t have to worry about scaling?**

Yes, it does, but **making users happy trumps everything else**. Your users are not happy to wait for your function to cold start so they can order their food. The cost of switching to a competitor is so low nowadays, what’s stopping them from leaving you?

You could also con­sid­er reduc­ing the impact of cold starts instead, by reduc­ing the duration of cold starts:

* Author­ your Lamb­da func­tions in a [lan­guage that doesn’t incur a high cold start time](https://read.acloud.guru/does-coding-language-memory-or-package-size-affect-cold-starts-of-aws-lambda-a15e26d12c76) — that is, Node.js, Python, or [Go](https://aws.amazon.com/blogs/compute/announcing-go-support-for-aws-lambda/)
* Use high­er mem­o­ry set­ting for func­tions on the crit­i­cal path, includ­ing inter­me­di­ate APIs
* Opti­miz­e your function’s depen­den­cies and pack­age size
* **Stay as far away from VPCs as you can!** Lamb­da cre­ates ENIs (elas­tic net­work inter­face) to the tar­get VPC, which can add up to 10s (yeah, you’re read­ing it right) to your cold start

There are also two oth­er fac­tors to con­sid­er:

* [Exe­cu­tions that are idle for a while would be garbage col­lect­ed](https://read.acloud.guru/how-long-does-aws-lambda-keep-your-idle-functions-around-before-a-cold-start-bf715d3b810)
* Exe­cu­tions that have been active for a while (some­where between 4 and 7 hours) would be garbage col­lect­ed, too

What about APIs that are sel­dom used? In that case, every invocation might be a cold start if too much time passes between invocations. To your users, these APIs are always slow, so they’re used less, and it becomes a vicious cycle.

For these, you can use a cron job (as in, a CloudWatch scheduled event with a Lambda function as target) to keep them warm. The cron job would run every 5–10 mins and ping the API with a special request. By keeping these APIs warm, your users would not have to endure cold starts.

![Image](https://cdn-media-1.freecodecamp.org/images/LGDH5Jx1YQ9H8Dqu4l4tEZXcz4kZoVMGNLn6)

This approach is less effective for busy functions with lots of concurrent executions. The ping message would only reach one of the concurrent executions, and there is no way to direct it to specific executions. In fact, there is no reliable way to know the exact number of concurrent executions for a function at all.

Also, if the number of concurrent user requests drops, then it’s in your best interest to let idle executions be garbage collected. After all, you wouldn’t want to pay for unnecessary resources you don’t need.

![Image](https://cdn-media-1.freecodecamp.org/images/tOP0ZmnqijAtz-rstaBmg7kgdWsWp16U1Ch3)

This post is not intend­ed to be your one-stop guide to AWS Lamb­da cold starts. It’s intended to illus­trate that talking about cold starts is a more nuanced dis­cus­sion than “_the first request._”

Cold starts are a char­ac­ter­is­tic of the plat­form that we have to live with. And we love the AWS Lamb­da plat­form and want to use it, as it deliv­ers on so many fronts. Nonetheless, it’s impor­tant to not let our own pref­er­ence blind us from what’s impor­tant. **Keeping our users hap­py and building a prod­uct that they love** is always the most important goal.

To that end, you do need to know the plat­form you’re build­ing on. With the cost of exper­i­men­ta­tion being so low, there’s no rea­son not to exper­i­ment with AWS Lamb­da your­self. Try to learn more about how it behaves and how you can make the most of it.

