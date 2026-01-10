---
title: Why you should sample debug logs in production
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-28T12:41:47.000Z'
originalURL: https://freecodecamp.org/news/why-you-should-sample-debug-logs-in-production-39d78ef3968d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*hF7dKQVn7EpWn3loQqECYQ.jpeg
tags:
- name: logging
  slug: logging
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Yan Cui

  It’s com­mon prac­tice to set your log lev­el to warning for pro­duc­tion due to
  traf­fic vol­ume. This is because you have to con­sid­er var­i­ous cost fac­tors:


  Cost of log­ging : Cloud­Watch Logs charges $0.50 per GB ingest­ed. In my e...'
---

By Yan Cui

It’s com­mon prac­tice to set your log lev­el to **warning** for pro­duc­tion due to traf­fic vol­ume. This is because you have to con­sid­er var­i­ous cost fac­tors:

* **Cost of log­ging** : _Cloud­Watch Logs_ charges $0.50 per GB ingest­ed. In my expe­ri­ence, this is often much high­er than the Lamb­da invo­ca­tion costs
* **Cost of stor­age** : _Cloud­Watch Logs_ charges $0.03 per GB per month, and its default reten­tion pol­i­cy is **Nev­er Expire**! A com­mon prac­tice is to ship your logs to anoth­er log aggre­ga­tion ser­vice and to set the reten­tion pol­i­cy to X days. See [this post](https://theburningmonk.com/2017/08/centralised-logging-for-aws-lambda/) for more details.
* **Cost of pro­cess­ing** : if you’re pro­cess­ing the logs with _Lamb­da_, then you also have to fac­tor in the cost of _Lamb­da_ invo­ca­tions.

But, doing so leaves us with­out **any** debug logs in pro­duc­tion. When a prob­lem hap­pens in pro­duc­tion, you won’t have the debug logs to help iden­ti­fy the root cause.

Instead, you have to waste pre­cious time deploying a new ver­sion of your code to enable debug log­ging. Not to men­tion that you shouldn’t for­get to dis­able debug log­ging when you deploy the fix.

With microser­vices, you often have to do this for more than one ser­vice to get all the debug mes­sages you need.

All these **increas­e the [mean time to recov­ery](https://en.wikipedia.org/wiki/Mean_time_to_recovery) (MTTR) dur­ing an inci­dent**. That’s not what we want.

![Image](https://cdn-media-1.freecodecamp.org/images/TV4JL3ABTOYu877SdNZOEje39xCsENsie6uy)

It doesn’t have to be like that.

There is a hap­py mid­dle ground between hav­ing no debug logs and hav­ing all the debug logs. Instead, we should sam­ple debug logs from a small per­cent­age of invo­ca­tions.

![Image](https://cdn-media-1.freecodecamp.org/images/-Sc5WbK9QBaTZ-S65EbI8zrIZGACvvZkAcqB)

I demoed how to do this in the _Log­ging_ chap­ter of my video course [Pro­duc­tion-Ready Server­less](https://bit.ly/production-ready-serverless). You need two basic things:

* a log­ger that lets you to change the log­ging lev­el dynam­i­cal­ly, for example via envi­ron­ment vari­ables
* a mid­dle­ware engine such as [mid­dy](https://github.com/middyjs/middy)

![Image](https://cdn-media-1.freecodecamp.org/images/kqho30Wb7OCBPap3XY2FvBtCSt9nUf-bGN--)

With _Lamb­da_, I don’t need most of the fea­tures from a ful­ly-fledged log­ger such as [pino](https://github.com/pinojs/pino). Instead, I pre­fer to use a sim­ple log­ger mod­ule like [this one](https://github.com/theburningmonk/manning-aws-lambda-in-motion/blob/master/lib/log.js). It’s writ­ten in a hand­ful of lines and gives me the basics:

* [struc­tured log­ging with JSON](https://theburningmonk.com/2018/01/you-need-to-use-structured-logging-with-aws-lambda/)
* abil­i­ty to log at dif­fer­ent lev­els
* abil­i­ty to con­trol the log lev­el dynam­i­cal­ly via envi­ron­ment vari­ables

Using _mid­dy_, I can cre­ate a [mid­dle­ware](https://github.com/theburningmonk/manning-aws-lambda-in-motion/blob/master/middleware/sample-logging.js) to dynam­i­cal­ly update the log lev­el to **debug**. It does this for a con­fig­urable per­cent­age of invo­ca­tions. At the end of the invo­ca­tion, the mid­dle­ware would restore the pre­vi­ous log lev­el.

![Image](https://cdn-media-1.freecodecamp.org/images/qO1K1e3vzJXADCmbdATAm92TS9epcO-AFkLw)

You might notice that we also have some spe­cial han­dling for when the invo­ca­tion errs.

![Image](https://cdn-media-1.freecodecamp.org/images/Gn15P9fo3QKW-HVk1Y1baSPgumRjfIhsAOl4)

This is to ensure we cap­ture the error with as much con­text as pos­si­ble, includ­ing:

* the unique AWS Request ID
* the invo­ca­tion event, so we can [replay the invo­ca­tion event local­ly](https://theburningmonk.com/2017/08/running-and-debugging-aws-lambda-functions-locally-with-the-serverless-framework-and-vs-code/) and debug the prob­lem
* the error mes­sage and stack­trace

Hav­ing debug logs for a small per­cent­age of invo­ca­tions is great. But when you’re deal­ing with microser­vices, you need to make sure that your debug logs cov­er an entire call chain.

That is the only way to put togeth­er a com­plete pic­ture of every­thing that hap­pened on that call chain. Oth­er­wise, you will end up with frag­ments of debug logs from many call chains but nev­er the com­plete pic­ture of one.

You can do this by for­ward­ing the deci­sion to turn on debug log­ging as a cor­re­la­tion ID. The next func­tion in the chain would respect this deci­sion, and pass it on. See [this post](https://theburningmonk.com/2017/09/capture-and-forward-correlation-ids-through-different-lambda-event-sources/) for more detail.

![Image](https://cdn-media-1.freecodecamp.org/images/FeWU7Hr6-zviBenJKyVZvNUp8GWlgyV1lVH5)

So that’s it, anoth­er pro tip on how to build observ­abil­i­ty into your server­less appli­ca­tion. If you want to learn more about how to go all in with server­less, check out my 10-step guide [here](https://blog.binaris.com/how-to-go-all-in-with-serverless-adoption/).

Until next time!

